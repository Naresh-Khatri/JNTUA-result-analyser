from django.db import models


class Student(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Subject(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=50)
    abb = models.CharField(max_length=10, null=True, blank=True)
    semester = models.IntegerField(default=1)
    credit = models.FloatField(default=0)

    def __str__(self):
        return f'{self.name}'


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.CharField(max_length=3, default='1')
    grade = models.CharField(max_length=2)
    passed = models.BooleanField(default=True)
    credit = models.FloatField(default=0)

    def __str__(self):
        return f'{self.student} {self.passed} {self.subject}'


class SemesterGPA(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    percentile = models.FloatField(default=0)
    sgpa = models.FloatField(default=0)
    semester = models.CharField(max_length=3, default='1')


class Feedback(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
