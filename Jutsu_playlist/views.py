from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import DeleteView , UpdateView , CreateView
from django.views.generic import ListView , DetailView
from .models import PlaylistJutsuModel 
from django.urls import reverse_lazy

# Create your views here.
class JutsuListView(View):
    def get(self, request):
        slids = PlaylistJutsuModel.objects.all().order_by('id')
        search_query = request.GET.get('q', '')
        if search_query:
            slids = slids.filter(name__icontains=search_query)
        return render(request, 'jutsu_list.html',{"object_list":slids, "search":search_query})

class JutsuDetailView(DetailView):
    model = PlaylistJutsuModel
    template_name = 'jutsu_detail.html'

class JutsuCreateView(LoginRequiredMixin , UserPassesTestMixin , CreateView):
    model = PlaylistJutsuModel
    template_name = 'jutsu_create.html'
    fields = ('photo','name' , 'about' , 'ninja')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff


class JutsuUpdateView(LoginRequiredMixin , UserPassesTestMixin, UpdateView):
    model = PlaylistJutsuModel
    template_name = 'jutsu_update.html'
    fields = ('photo','name' , 'about' , 'ninja')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class JutsuDeleteView(LoginRequiredMixin , UserPassesTestMixin, DeleteView):
    model = PlaylistJutsuModel
    template_name = 'jutsu_delete.html'
    success_url = reverse_lazy('jutsu_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user