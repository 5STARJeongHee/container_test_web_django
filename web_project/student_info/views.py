from django.shortcuts import render

from .models import Students
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    students_list = Students.objects.order_by('name')
    context = {'students_list': students_list}
    return render(request, 'student_info/students_list.html', context)

def sending(request):

    if request.method == 'POST':
        name = request.POST['name']
        student_num = request.POST['student_num']
        phone_num = request.POST['phone_num']
        email = request.POST['email']

        new_student = Students(name = name, student_num=student_num, phone_num=phone_num, email=email)

        new_student.save()

        students_list = Students.objects.order_by('name')
        context = {'students_list': students_list}
        return render(request, 'student_info/students_list.html', context)



