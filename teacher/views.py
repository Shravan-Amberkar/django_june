from django.shortcuts import render
from teacher.models import *

def index(request):
    return render(request, 'teacher/home.html')


def contact(request):
    return render(request, 'teacher/contact.html')

def contact_form(request):
    # fetching parameter
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    email = request.POST['email']
    mobile = request.POST['mobile']

    # save to database
    new_record = TeacherCustomerContact(first_name = first_name, second_name = last_name, email = email,mobile = mobile)
    new_record.save()

    return render(request, 'teacher/thankyou.html', {'first_name':first_name, 'last_name': last_name,'email':email, 'mobile':mobile })

def about(request):
    return render(request, 'teacher/about.html')
