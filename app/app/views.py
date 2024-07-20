from django.http import HttpResponse
# app/views.py
from django.shortcuts import render

import datetime

def home(request):

    isActive = True
    if request.method=='POST':
        check=request.POST.get("check")
        print(check)
        if check is None: isActive=False
        else: isActive= True

    date= datetime.datetime.now()
    
    name="Iampragati"
    list_of_program= ['write a program to check even or odd',
           'write a program to check prime no',
           'write a program to check pelindrome no',
           'WAP for a pascal triangle']
    student_data={
            'student_name':'pragati',   
            'student_college':"xyz",
            'student_city':"jabalpur"
            }       
    data={
          'date':date,  
          'isActive':isActive, 
          'name':name,
          'list_of_programs':list_of_program, 
          'student_data':student_data
          }         
    return render(request, 'home.html', data)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

