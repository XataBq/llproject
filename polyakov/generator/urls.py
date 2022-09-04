from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('gen/', gen, name='gen'),
    path('gen/<int:pk>/', ready_var, name='ready_var')
]
