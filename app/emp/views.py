# app/views.py

from django.shortcuts import render, redirect
from .models import Emp
# View for the home page
def emp_home(request):
    emps=Emp.objects.all()
    return render(request, 'emp/home.html',{'emps':emps})

# View for adding an employee
def add_emp(request):
    if request.method == "POST":
        #datafetch
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        #validation
        
  
        #create model object and set the data
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True  
        #save the data
        e.save()

        #prepare msg
        # You can add logic here to process form data if needed
        print("data is coming")
        return redirect("/emp/home/")
    return render(request, 'emp/add_emp.html')


def delete_emp(request,emp_id):
    print(emp_id)
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")
 

def update_emp(request, emp_id):
    emp = Emp.objects.get(pk=emp_id)

    if request.method == "POST":
        # Update employee data from the form
        emp.name = request.POST.get("emp_name")
        emp.emp_id = request.POST.get("emp_id")
        emp.phone = request.POST.get("emp_phone")
        emp.address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp.department = request.POST.get("emp_department")
        emp.working = bool(emp_working)

        emp.save()
        return redirect("/emp/home/")

    return render(request, "emp/update_emp.html", {'emp': emp})
