from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "fn", "ln", "user"]


admin.site.register(Student, StudentAdmin)
