from django.urls import path
from .views import SlideCreateView , SlideDeleteView , SlideUpdateView , SlideDetailView

urlpatterns = [
    path('create/' , SlideCreateView.as_view() , name='slide_create'),
    path('update/<int:pk>/' , SlideUpdateView.as_view() , name='slide_update'),
    path('delete/<int:pk>/' , SlideDeleteView.as_view() , name='slide_delete'),
    path('detail/<int:pk>/' , SlideDetailView.as_view() , name='slide_detail')
]