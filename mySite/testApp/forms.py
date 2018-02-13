from django import forms
from testApp.models import *

class TeacherForm(forms.ModelForm):
  class Meta:
      model = Teacher
      fields = '__all__'

class StudentForm(forms.ModelForm):
  class Meta:
      model = Student
      fields = '__all__'

class ClassForm(forms.ModelForm):
    class Meta:
        model = MyClass
        fields = '__all__'
