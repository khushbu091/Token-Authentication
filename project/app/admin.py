from django.contrib import admin
from .models import StudentModel, EmployeeModel, CarModel

# Register your models here.

admin.site.register(StudentModel)
admin.site.register(EmployeeModel)
admin.site.register(CarModel)


