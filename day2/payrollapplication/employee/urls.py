from django.urls import path
from . import views
urlpatterns=[
    path('',views.register_employee, name='employee_register'),
    path('list/', views.employee_list, name='employee_list'),
    path('list/data', views.employee_list_json, name='employee_list_json'),
    path('list/json/', views.employee_list_json_view, name='employee_list_json_view'),
    path('update/<int:emp_id>/', views.employee_edit, name='employee_edit'),
    path('delete/<int:emp_id>/', views.employee_delete, name='employee_delete'),
    path('report/csv/', views.employee_report_csv, name='employee_report_csv'), 
    path('report/xml/', views.employee_report_xml, name='employee_report_xml'), # This line is redundant and can be removed
    path('uploadexcel/', views.upload_excel, name='upload_excel'),
]