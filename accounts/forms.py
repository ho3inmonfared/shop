from django.contrib.auth.forms import UserChangeForm,UserCreationForm

from . import models

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=models.CustomUser
        fields=UserCreationForm.Meta.fields
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=models.CustomUser
        fields=UserChangeForm.Meta.fields 