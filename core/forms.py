from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from core.models import Record

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=TextInput())
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

# Создать запись
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields=['first_name', 'last_name', 'phone', 'email', 'country', 'address', 'city', 'province']
# Создать запись
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields=['first_name', 'last_name', 'email', 'phone', 'country', 'address', 'city', 'province']