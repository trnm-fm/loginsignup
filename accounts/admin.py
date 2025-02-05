from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model=User
    list_display =('email','is_superuser','is_staff')
    list_filter =('email','is_superuser','is_staff')
    searching_fields =('email',)
    ordering = ('email',)
    fieldsets =(
        ('Authentication',{
            "fields":(
                'email',
                'password'
            ),
        }),
        ('Permissions',{
            "fields":(
                'is_superuser',
                'is_staff',
                'is_active'
            ),
        }),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':(('email'),('password1'),('password2'),('is_staff'),('is_superuser'),('is_active'),),
        }),
    )

admin.site.register(User,CustomUserAdmin)