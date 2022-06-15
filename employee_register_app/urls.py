from django.urls import path
from . import views

app_name= 'employee'

urlpatterns=[
    path('',views.LoadEmployee),
    path('employeeDetails/',views.EmployeeDetails),
    path('employee_ID/<pk>',views.EmployeeID,name='employee_ID'),
    path('deleteemployee/<pk>',views.DeleteEmployee,name='deleteemployee'),
    path('updateemployee/<pk>',views.UpdateEmployee,name='updateemployee'),
]
