
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "first_name", "last_name",
                    "is_staff", "last_login")
    fieldsets = (
        (None, {"fields": ("email", "password",
                           "first_name", "last_name", "last_login")}),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser",
                        "groups", "user_permissions")},
        ),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": (
            "email", "password1", "password2")}),
    )

    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ("groups", "user_permissions")


admin.site.register(CustomUser, CustomUserAdmin)
