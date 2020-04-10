from django.contrib import admin
from django.contrib.auth import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'street', 'city',
                    'state', 'zip_code', 'phone', 'age', 'is_staff', ]
    admin.site.register(CustomUser, CustomUserAdmin)
