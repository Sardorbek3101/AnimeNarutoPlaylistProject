from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView ,UpdateView , DeleteView
from .forms import CustomUserCreationForm
from .models import CustomUser
# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ChangeView(LoginRequiredMixin , UserPassesTestMixin, UpdateView):
    model = CustomUser  
    fields = ('username' , 'first_name' , 'last_name' , 'email' , 'phone_number' , 'photo')
    template_name = 'registration/change.html'

    def test_func(self):
        obj = self.get_object()
        return obj.pk == self.request.user.pk


class UserDeleteView(LoginRequiredMixin , UserPassesTestMixin ,DeleteView):
    model = CustomUser
    template_name = 'registration/delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.pk == self.request.user.pk

class ProfileView(LoginRequiredMixin , UserPassesTestMixin ,DetailView):
    model = CustomUser
    template_name = 'profile.html'
 
    def test_func(self):
        obj = self.get_object()
        return obj.pk == self.request.user.pk
