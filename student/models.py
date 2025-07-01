from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
import re

class Student(models.Model):
    roll_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="Age must be between 1 and 100"
    )
    marks = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
        help_text="Marks must be between 0 and 100"
    )

    def clean(self):
        if not re.match(r'^[A-Za-z ]+$', self.name):
            raise ValidationError({'name': "Name must contain only letters (e.g. Raj, Sneha)"})

    def __str__(self):
        return f"{self.roll_number} - {self.name}"



