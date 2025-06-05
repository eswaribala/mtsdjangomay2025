from django.db import models

# Create your models here.
from django.db import models

class Gender(models.TextChoices):
    MALE = 'M',
    FEMALE = 'F',
    OTHER = 'O'
# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    hire_date = models.DateField()
    job_title = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    emp_id=models.AutoField(primary_key=True)
    gender=models.TextField(
        choices=Gender.choices,
        default=Gender.MALE
    )

class Address(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    

   
