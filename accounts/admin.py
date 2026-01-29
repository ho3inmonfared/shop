from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import forms , models

@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form=forms.CustomUserCreationForm
    form=forms.CustomUserChangeForm
    model=models.CustomUser
    
    list_display=('username','email','is_staff','is_active', )
    list_filter=('is_staff','is_active',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    search_fields=('username','email')
    ordering=('username',)

    
