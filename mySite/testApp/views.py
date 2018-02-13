from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from testApp.models import *
from testApp.forms import *

class TeacherView(TemplateView):
    template_name = "teacher.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        teachers = Teacher.objects.all()
        context['teachers'] = teachers

        return context

def teacherFormView(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/teacher')

    form = TeacherForm()
    return render(request, 'teacher_form.html', {'form': form})

class StudentView(TemplateView):
    template_name = "student.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        students = Student.objects.all()
        context['students'] = students

        return context

def studentFormView(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/student')

    form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

class ClassView(TemplateView):
    template_name = "class.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        classes = MyClass.objects.all()
        context['classes'] = classes

        return context

def classFormView(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/class')

    form = ClassForm()
    return render(request, 'class_form.html', {'form': form})
