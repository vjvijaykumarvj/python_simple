from django.shortcuts import render,redirect
from .models import Employee
# Create your views here.

def LoadEmployee(request):
    employee_list=Employee.objects.all
    emp_dict={
        'employeeFBV' :  employee_list
    }
    return render(request,'employee_register_app/list_emp.html',context=emp_dict)

def EmployeeDetails(request):
    if request.method=='GET':
        return render(request,'employee_register_app/employee_detail.html')
    elif request.method == 'POST':
        eno = request.POST.get('emp_number')
        name = request.POST.get('name')
        age = request.POST.get('age')
        salary = request.POST.get('salary')
        address = request.POST.get('address')
        employee = Employee(eno=eno, name=name, age=age, salary=salary, address=address)
        employee.save()
        return redirect('/employee/')

def EmployeeID(request,pk):
    employee=Employee.objects.get(id=pk)
    emp_dict={
        'employee' : employee
    }
    return render(request,'employee_register_app/employeeID.html',context=emp_dict)

def DeleteEmployee(request,pk):
    emp=Employee.objects.get(id=pk)
    emp.delete()
    return redirect('/employee/')

def UpdateEmployee(request,pk):
    if request.method=='GET':
        employee=Employee.objects.get(id=pk)
        emp_dict={
            'employee' : employee
        }
        return render(request,'employee_register_app/employee_detail.html',context=emp_dict)
    elif request.method=='POST':
        employee=Employee.objects.get(id=pk)
        eno = request.POST.get('emp_number')
        name = request.POST.get('name')
        age = request.POST.get('age')
        salary = request.POST.get('salary')
        address = request.POST.get('address')
        #employee = Employee(eno=eno, name=name, age=age, salary=salary, address=address)
        employee.eno = eno
        employee.name = name
        employee.age = age
        employee.salary = salary
        employee.address = address
        employee.save()
    return redirect('/employee/')





