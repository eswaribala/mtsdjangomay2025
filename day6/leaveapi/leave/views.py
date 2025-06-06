from django.shortcuts import render

from confluent_kafka import Consumer, KafkaError
from dotenv import load_dotenv
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from drf_yasg import openapi
from mongoengine import connect


@api_view(['GET'])
def showconsumed_data(request):
    '''
    read from mongo db and show the data
    '''''
    return Response({
        "message": "Data consumed successfully. Check the console for output."
    })