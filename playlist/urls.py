from django.urls import path
from .views import NinjaDeleteView,NinjaListView , NinjaDetailView ,NinjaCreateView, NinjaUpdateView

urlpatterns = [
    path('', NinjaListView.as_view() , name='ninja_list'),
    path('<int:pk>/' , NinjaDetailView.as_view() , name='detail'),
    path('create/' , NinjaCreateView.as_view() , name='ninja_create'),
    path('change/<int:pk>/' , NinjaUpdateView.as_view() , name='ninja_update'),
    path('delete/<int:pk>/' , NinjaDeleteView.as_view() , name='ninja_delete'),
]
