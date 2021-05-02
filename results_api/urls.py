from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('students', views.StudentViewSet)
router.register('subjects', views.SubjectViewSet)
router.register('results', views.ResultViewSet)
router.register('semestergpa', views.SemesterGPAViewSet)
router.register('feedbacks', views.FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]