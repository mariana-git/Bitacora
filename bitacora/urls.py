from django.urls import path

from .models import *
from .views import *


urlpatterns = [
    path('listar/', BitacoraListView.as_view(),name='bitacora_list'), 
    path('crear/', BitacoraCreateView.as_view(),name='bitacora_add'), 
    path('ver/<pk>', BitacoraDetailView.as_view(),name='bitacora_detail'), 
    path('modificar/<pk>', BitacoraUpdateView.as_view(),name='bitacora_change'), 
    path('eliminar/<pk>', BitacoraDeleteView.as_view(),name='bitacora_delete'), 

    # Perfil de usuarios
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),

]
