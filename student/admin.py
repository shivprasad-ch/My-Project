from django.contrib import admin
from .models import Student
from django.core.exceptions import ValidationError

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'name', 'age', 'marks')
    search_fields = ('name', 'roll_number')
    ordering = ('roll_number',)

    fieldsets = (
        ('Student Info', {
            'fields': ('roll_number', 'name'),
        }),
        ('Academic Info', {
            'fields': ('age', 'marks'),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.full_clean()
        super().save_model(request, obj, form, change)