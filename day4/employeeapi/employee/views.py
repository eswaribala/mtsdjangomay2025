import json
import os
import time
from django.http import JsonResponse
from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from employee.kafkaproducerconfiguration import acked, kafka_configure
from employee.models import Employee
from employee.serializers import EmployeeSerializer
from dotenv import load_dotenv
from confluent_kafka import Consumer
from django.core.cache import cache
from resilient_caller import resilient_call, RETRY_EVENT
load_dotenv()
@swagger_auto_schema(
    methods=['post'],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['first_name','last_name','phone_number', 'email', 'status','gender','job_title','salary','hire_date'],
        properties={
            'first_name': openapi.Schema(type=openapi.TYPE_STRING),
            'last_name': openapi.Schema(type=openapi.TYPE_STRING),
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING),
            'status': openapi.Schema(type=openapi.TYPE_BOOLEAN),
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'gender': openapi.Schema(type=openapi.TYPE_STRING),
            'job_title': openapi.Schema(type=openapi.TYPE_STRING),
            'salary': openapi.Schema(type=openapi.TYPE_NUMBER),
            'hire_date': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME)       

        },
    ),
    operation_description='Create Employee',
    responses={200: ""}
)
@api_view(['GET', 'POST'])
# Create your views here.
def employee_list(request):
    if request.method == 'GET':
        cache_key='employee_data'
        #print(cache.has_key())
        
        data=cache.get(cache_key)
        
        print(data)
        if data is None:
            #time.sleep(2)
            employees=Employee.objects.all() 
            serializer = EmployeeSerializer(employees, many=True)
            cache.set(cache_key,json.dumps(serializer.data),timeout=60)
            return Response(serializer.data)
        else:
            return JsonResponse(data,safe=False)
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

producer = kafka_configure()
@api_view(['GET','DELETE'])
def employee_transactions(request,pk):
    employee = Employee.objects.get(pk=pk)
    #topicName=os.getenv('KAFKA_TOPIC_NAME')
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        jsonData = json.dumps(serializer.data)
   
        producer.produce(os.getenv("KAFKA_TOPIC_NAME"), key="key", value=jsonData, callback=acked)

            # Wait up to 1 second for events. Callbacks will be invoked during
            # this method call if the message is acknowledged.
        producer.poll(1)
            # Customize the response for a successful creation
        response_data = {
                'message': 'Transaction published successfully!',
                'data': serializer.data,
            }
            
           
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=204)  # No content

@swagger_auto_schema(
    methods=['put'],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['phone_number', 'email'],
        properties={            
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING),            
            'email': openapi.Schema(type=openapi.TYPE_STRING)                  

        },
    ),
    operation_description='Update Employee',
    responses={200: ""}
)
@api_view(['PUT'])
def employee_update(request,pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'PUT':
        try:
            data=json.loads(request.body)
            employee= Employee.objects.get(pk=pk)
            if 'phone_number' in data:
                employee.phone_number = data['phone_number']
            if 'email' in data:
                employee.email = data['email']
            if 'phone_number' not in data and 'email' not in data:
                return Response({"error": "At least one field must be provided for update."}, status=400)
            if 'phone_number' in data or 'email' in data:
                employee.save(update_fields=['phone_number', 'email'])
            return Response({"message": "Employee updated successfully."}, status=200)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found."}, status=404)
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON format."}, status=400)
    return Response({"error": "Invalid request method."}, status=405)

def consume_kafka_message():
    conf = {
        'bootstrap.servers': os.getenv('bootstrap.servers'),
        'security.protocol': os.getenv('security.protocol'),
        'sasl.mechanism': os.getenv('sasl.mechanism'),  
        'sasl.username': os.getenv('sasl.username'),
        'sasl.password': os.getenv('sasl.password'),
        'client.id': os.getenv('client.id'),
        'group.id': 'django-api-consumer',
        'auto.offset.reset': 'earliest',
    }

    consumer = Consumer(conf)
    topic = os.getenv('KAFKA_TOPIC_NAME')
    consumer.subscribe([topic])
    
    msg = consumer.poll(10.0)  # wait max 10 sec

    if msg is None:
        return {"status": "no message available"}
    elif msg.error():
        return {"error": str(msg.error())}

    value = msg.value().decode("utf-8")
    consumer.close()
    
    return {"message": value}
@api_view(['GET'])
def kafka_consume_view(request):
    result = consume_kafka_message()  # This returns a dict
    return Response(result)  # ← Wrap it in DRF Response


@api_view(["GET"])
def test_api(request):
    api_url = os.getenv("api_url")
    fallback_api_url=os.getenv("fallback_api_url")
    print(api_url)
    if request.method == 'GET':
        response = fetch_test_api(api_url, retries=5, delay=5,  exceptions={'all': RETRY_EVENT})
        print(response)
        if response is None:
            response = fetch_test_api(fallback_api_url, retries=5, delay=5, exceptions={'all': RETRY_EVENT})
            if response is None:
                response_data = {
                    'message': 'Test API not available'
                }
                return Response(response_data, status=404)
        return Response(response.json())
    


@resilient_call(max_elapsed_time=2000)
def fetch_test_api(url):
    print(f"Accessing API{url}")
    return requests.get(url)
