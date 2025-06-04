from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from employee.models import Employee
from employee.serializers import EmployeeSerializer
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
        employees=Employee.objects.all() 
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)