from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.views.generic.edit import DeleteView , UpdateView , CreateView
from django.views.generic import ListView , DetailView
from .models import SlideModel
from django.urls import reverse_lazy

# Create your views here.
class SlideListView(ListView):
    model = SlideModel
    template_name = 'home.html'

class SlideDetailView(LoginRequiredMixin , UserPassesTestMixin , DetailView):
    model = SlideModel
    template_name = 'slide_detail.html'
    
    def test_func(self):
        return self.request.user.is_staff
class SlideCreateView(LoginRequiredMixin , UserPassesTestMixin , CreateView):
    model = SlideModel
    template_name = 'slide_create.html'
    fields =  ('title','img1' ,'name1','body1' , 'img2' , 'name2','body2' ,'img3' ,'name3','body3' ,'img4' ,'name4','body4', 'img5','name5','body5')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff

class SlideUpdateView(LoginRequiredMixin , UserPassesTestMixin, UpdateView):
    model = SlideModel
    template_name = 'slide_update.html'
    fields = ('title','img1' ,'name1','body1' , 'img2' , 'name2','body2' , 'img3' ,'name3','body3' ,'img4' ,'name4','body4' ,'img5','name5','body5')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class SlideDeleteView(LoginRequiredMixin , UserPassesTestMixin, DeleteView):
    model = SlideModel
    template_name = 'slide_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user