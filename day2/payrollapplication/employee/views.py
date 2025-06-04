from io import BytesIO
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from .forms import EmployeeForm, EmployeeUpdateForm, ExcelUploadForm
from .models import Employee,Gender
import pandas as pd

# Create your views here.
def register_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        print("Form data:", form.data)  # Debugging line to check form data
        if form.is_valid():
            form.save()
            return redirect('employee_list')
        else:
            print("Form errors:", form.errors)
    else:
        form = EmployeeForm()
    gender_choices=Gender.choices
    return render(request, 'employee_register.html', {'gender_choices': gender_choices})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})
def employee_list_json_view(request):
    return render(request, 'employee_list_json.html')
def employee_list_json(request):
    employees = Employee.objects.all()
    employee_data = []
    columns=[{'data':key,'title':key.replace('_', ' ').capitalize()} for key in employees[0].__dict__.keys() if not key.startswith('_')]
    #print("Columns:", columns)  # Debugging line to check columns
    for emp in employees:
        employee_data.append({
            'emp_id': emp.emp_id,
            'first_name': emp.first_name,   
            'last_name': emp.last_name,
            'email': emp.email,
            'phone_number': emp.phone_number,
            'salary': emp.salary,
            'job_title': emp.job_title,
            'status': emp.status,
            'gender': emp.gender,
            'hire_date': emp.hire_date.strftime('%Y-%m-%d')
        })
    return JsonResponse({'columns':columns,'data': employee_data})


def employee_edit(request, emp_id):
    employee = get_object_or_404(Employee, pk=emp_id)
    
    if request.method == 'POST':
        form = EmployeeUpdateForm(request.POST, instance=employee)  
        print(form.data)
        if form.is_valid():
            print(form.data)
            form.save()
            return redirect('employee_list')  # or use reverse('employee_list')
        else:
            print(form.errors)
    else:
        form = EmployeeUpdateForm(instance=employee)
    return render(request, 'employee_edit.html', {'form': form, 'employee': employee})


def employee_delete(request, emp_id):
    employee = get_object_or_404(Employee, pk=emp_id)
    
    employee = Employee.objects.get(emp_id=emp_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_delete.html', {'employee': employee})

def employee_report_csv(request):
    employees = Employee.objects.all().values()
    df=pd.DataFrame.from_records(employees)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'
    df.to_csv(path_or_buf=response, index=False, encoding='utf-8-sig')
    return response

def employee_report_xml(request):
    employees = list(Employee.objects.all().values())
    df=pd.DataFrame(employees)
    xml_data = df.to_xml(root_name='employees', row_name='employee', index=False)
    response = HttpResponse(xml_data, content_type='application/xml')
    response['Content-Disposition'] = 'attachment; filename="employees.xml"'
    return response
def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            try:
                # Read Excel file into DataFrame
                df = pd.read_excel(BytesIO(excel_file.read()))

                # Check required columns exist
                required_columns = {'first_name', 'last_name', 'email','phone_number','salary', 'job_title','status', 'hire_date', 'gender'}
                if not required_columns.issubset(set(df.columns)):
                    messages.error(request, "Excel file must have columns: " + ", ".join(required_columns))
                    return redirect('upload_excel')

                # Insert rows into database
                for _, row in df.iterrows():
                    Employee.objects.create(
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        email=row['email'],
                        hire_date=row['hire_date'],
                        job_title=row['job_title'],
                        salary=row['salary'],
                        gender=row['gender'],
                        status=row['status'],
                        phone_number=row['phone_number']
                    )

                messages.success(request, "Employees uploaded successfully.")
                return redirect('upload_excel')

            except Exception as e:
                messages.error(request, f"Error processing file: {str(e)}")
                return redirect('upload_excel')
    else:
        form = ExcelUploadForm()
    return render(request, 'upload_excel.html', {'form': form})
            
      