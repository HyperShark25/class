from django.contrib import admin
from .models import Subject, Student, Teacher, Enrollment, Track


class SubjAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class StAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class TAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class EnAdmin(admin.ModelAdmin):
    list_display = ["id"]


class TrAdmin(admin.ModelAdmin):
    list_display = ["id", "track"]


admin.site.register(Subject, SubjAdmin)
admin.site.register(Student, StAdmin)
admin.site.register(Teacher, TAdmin)
admin.site.register(Enrollment, EnAdmin)
admin.site.register(Track, TrAdmin)
