from django.db import models

class Teacher(models.Model):
    f_name = models.CharField(max_length=16)
    l_name = models.CharField(max_length=16)


class Student(models.Model):
    #学校区分
    ELEMENTARY = 0
    JUNIOR = 1
    SENIOR = 2

    f_name = models.CharField(max_length=16)
    l_name = models.CharField(max_length=16)

    school = models.IntegerField() #学校区分
    grade = models.IntegerField() #学年


class MyClass(models.Model):
    #授業時間
    # 1 : 13:15 - 14:45
    # 2 : 14:50 - 16:20
    # 3 : 16:50 - 18:20
    # 4 : 18:25 - 19:55
    # 5 : 20:00 - 21:30

    #教科
    MATH = 0
    ENGLISH = 1
    JAPANESE = 2
    SCIENCE = 3
    SOCIAL = 4

    #授業区分
    # 0 : 通常授業
    # 1 : 講習会

    date = models.DateField()
    time = models.IntegerField() #授業時間
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.IntegerField() #教科
    kind = models.IntegerField() #授業区分
    about = models.CharField(max_length=256)
