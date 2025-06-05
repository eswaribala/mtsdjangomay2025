from rest_framework import serializers
from .models import Employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee  # Assuming the Employee model is defined in employee/models.py
        fields = '__all__'  # Include all fields from the Employee model
        