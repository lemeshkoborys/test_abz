from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'position',
        'join_date',
        'salary',
        'chief'
    )

    list_filter = (
        'chief',
    )
