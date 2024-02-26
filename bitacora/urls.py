from django.urls import path

from .models import *
from .views import *


urlpatterns = [
    path('bitacora/listar', BitacoraListView.as_view(),name='bitacora_list'), 
    path('bitacora/crear', BitacoraCreateView.as_view(),name='bitacora_add'), 
    path('bitacora/ver/<pk>', BitacoraDetailView.as_view(),name='bitacora_detail'), 
    path('bitacora/modificar/<pk>', BitacoraUpdateView.as_view(),name='bitacora_change'), 
    path('bitacora/eliminar/<pk>', BitacoraDeleteView.as_view(),name='bitacora_delete'), 

    # Perfil de usuarios
    path('perfil/editar', EditProfileView.as_view(), name='edit_profile'),

]
