from django import forms
from .models import Employee
#DTO: This code defines a Django form for the Employee model, allowing for easy creation and validation of employee data.
class EmployeeForm(forms.ModelForm):
    #inner class which is configuring metadata for model
    #it tells django how to handle the model
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['email','phone_number']

class ExcelUploadForm(forms.Form):
    file = forms.FileField()
    
    