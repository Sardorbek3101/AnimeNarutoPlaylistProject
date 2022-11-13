from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.forms import TextInput
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username' , 'first_name' , 'last_name' , 'email' , 'phone_number')
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username' , 'first_name' , 'last_name' , 'email' , 'phone_number' , 'photo')

