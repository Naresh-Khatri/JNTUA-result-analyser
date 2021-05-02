from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters

from results_api import serializers
from results_api import models


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=student__id', 'subject__semester',)


class SemesterGPAViewSet(viewsets.ModelViewSet):
    queryset = models.SemesterGPA.objects.all()
    serializer_class = serializers.SemesterGPASerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('semester', 'student__name','=student__id')
