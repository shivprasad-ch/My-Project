from django import forms
from .models import Student
import re

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll_number', 'name', 'age', 'marks']
        widgets = {
            'roll_number': forms.NumberInput(attrs={'placeholder': 'Example: 101'}),
            'name': forms.TextInput(attrs={'placeholder': 'Example: Raj, Sneha'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Enter Age (1–100)'}),
            'marks': forms.NumberInput(attrs={'placeholder': 'Enter Marks (0–100)'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match("^[A-Za-z ]+$", name):
            raise forms.ValidationError("Name must contain only letters.")
        return name

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 1 or age > 100:
            raise forms.ValidationError("Age must be between 1 and 100.")
        return age

    def clean_marks(self):
        marks = self.cleaned_data['marks']
        if marks < 0.0 or marks > 100.0:
            raise forms.ValidationError("Marks must be between 0 and 100.")
        return marks