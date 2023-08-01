from app2.models import Student
from rest_framework import serializers


class StudSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = '__all__'
