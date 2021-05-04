from rest_framework import serializers
from results_api.models import Student, Subject, Result, SemesterGPA, Feedback


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'
        
class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields= ['url', 'id', 'name', 'abb', 'semester', 'credit']

class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = '__all__'
        depth=1
        #fields = ['id', 'student', 'subject']

class SemesterGPASerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SemesterGPA
        fields = '__all__'
        depth=1


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
        