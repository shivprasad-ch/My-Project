from rest_framework import serializers
from .models import Student
import re

class StudentSerializer(serializers.ModelSerializer):

    # ✅ Custom validation for 'name' field
    def validate_name(self, value):
        if not re.match(r'^[A-Za-z ]+$', value):
            raise serializers.ValidationError("Name must contain only letters (e.g. Raj, Sneha)")
        return value

    class Meta:
        model = Student
        fields = '__all__' 