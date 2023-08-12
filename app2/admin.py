from django.contrib import admin
from .models import Subject, Student, Teacher, Enrollment


class SubjAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class StAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class TAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class EnAdmin(admin.ModelAdmin):
    list_display = ["id"]



admin.site.register(Subject, SubjAdmin)
admin.site.register(Student, StAdmin)
admin.site.register(Teacher, TAdmin)
admin.site.register(Enrollment, EnAdmin)
