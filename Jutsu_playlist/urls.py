from django.urls import path
from .views import JutsuCreateView , JutsuDetailView , JutsuDeleteView , JutsuListView , JutsuUpdateView

urlpatterns = [
    path('', JutsuListView.as_view() , name='jutsu_list'),
    path('<int:pk>/' , JutsuDetailView.as_view() , name='jutsu_detail'),
    path('create/' , JutsuCreateView.as_view() , name='jutsu_create'),
    path('change/<int:pk>/' , JutsuUpdateView.as_view() , name='jutsu_update'),
    path('delete/<int:pk>/' , JutsuDeleteView.as_view() , name='jutsu_delete'),
]
