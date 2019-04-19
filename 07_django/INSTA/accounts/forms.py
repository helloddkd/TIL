from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = User

