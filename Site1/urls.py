from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('encrypt/', views.encrypt_file, name='encrypt'),
    path('decrypt/', views.decrypt_file, name='decrypt'),
]
