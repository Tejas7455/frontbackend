from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class Employeeadmin(admin.ModelAdmin):
    list_display = ['eid','ename','esal','addr']
