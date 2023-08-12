from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

UM = get_user_model()


class UMAdmin(UserAdmin):
    model = UM
    list_display = ["id", "username", "email", "is_admin", "form_id"]
    fieldsets = [["Edit Info", {"fields": ["email", "username", "date_of_birth", "is_admin","password"]}]]
    add_fieldsets = [["Create Account", {"fields": ["email", "username", "date_of_birth", "is_admin", "password1", "password2"]}]]
    list_filter = []
    filter_horizontal = []
    ordering = ("email",)


admin.site.register(UM, UMAdmin)

