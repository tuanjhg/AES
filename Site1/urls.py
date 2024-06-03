from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('encrypt/', views.encrypt_file, name='encrypt'),
    path('decrypt/', views.decrypt_file, name='decrypt'),
    path('decrypt_data/', views.decrypt_file1, name='decrypt_data'),
    path('create_stuff/', views.create_stuff, name='create_stuff'),
    path('stuff_list/', views.stuff_list, name='stuff_list'),
    path('encrypt_all_data/', views.encryptData, name='encrypt_all_data'),
    path('delete_stuff/<int:stuff_id>/', views.delete_stuff, name='delete_stuff'),
#    path('display/', views.display_decrypted_data, name = "display")
]
