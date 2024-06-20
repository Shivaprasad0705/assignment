from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('factorial/', views.calculate_factorial, name='calculate_factorial'),
]
