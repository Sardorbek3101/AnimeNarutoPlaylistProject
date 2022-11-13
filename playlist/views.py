from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.views.generic.edit import DeleteView , UpdateView , CreateView
from django.views.generic import ListView , DetailView
from .models import PlaylistPersonModel
from django.urls import reverse_lazy

# Create your views here.
class NinjaListView(ListView):
    model = PlaylistPersonModel
    template_name = 'person_list.html'

class NinjaDetailView(DetailView):
    model = PlaylistPersonModel
    template_name = 'ninja_detail.html'

class NinjaCreateView(LoginRequiredMixin , UserPassesTestMixin , CreateView):
    model = PlaylistPersonModel
    template_name = 'ninja_create.html'
    fields = ('photo','name' , 'role' , 'about' , 'jutsu')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff


class NinjaUpdateView(LoginRequiredMixin , UserPassesTestMixin, UpdateView):
    model = PlaylistPersonModel
    template_name = 'ninja_update.html'
    fields = ('photo','name' , 'role' , 'about' , 'jutsu')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class NinjaDeleteView(LoginRequiredMixin , UserPassesTestMixin, DeleteView):
    model = PlaylistPersonModel
    template_name = 'ninja_delete.html'
    success_url = reverse_lazy('ninja_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
