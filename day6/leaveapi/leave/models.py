from django.db import models
import mongoengine as me
# Create your models here.
"""""
class Employee(me.Document):
    first_name = me.StringField(required=True, max_length=50)
    last_name = me.StringField(required=True, max_length=50)
    email = me.StringField(required=True, max_length=100, unique=True)
    phone_number = me.StringField(max_length=15, unique=True)
    hire_date = me.DateTimeField(required=True)
    job_title = me.StringField(required=True, max_length=50)
    salary = me.DecimalField(required=True, precision=2, min_value=0)
    status = me.BooleanField(default=True)
    emp_id=me.IntField(required=True, unique=True)
    gender=me.StringField(required=True,choices=["M","F","O"],max_length=1)

class Employee(me.Document):
    metadata = me.DictField(required=True)
"""
class Employee(me.DynamicDocument):
    pass