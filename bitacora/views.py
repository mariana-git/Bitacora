from django.contrib.auth.mixins import PermissionRequiredMixin,UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from .forms import *
from .models import *

class BitacoraListView(PermissionRequiredMixin,ListView):
    permission_required = 'bitacora.view_bitacora'
    model = bitacora
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener todos los usuarios únicos que tienen entradas en la bitácora
        usuarios_bitacora = self.model.objects.values('usuario__id', 'usuario__username').distinct()
        # Formar un conjunto de tuplas con los IDs y nombres de usuario
        opciones_usuario_set = {(usuario['usuario__id'], usuario['usuario__username']) for usuario in usuarios_bitacora}
        # Convertir el conjunto en una lista
        opciones_usuario = list(opciones_usuario_set)
        # Agregar la lista de opciones de usuario al contexto
        context['opciones_usuario'] = opciones_usuario
        return context


    #  devuelve queryset completo o filtrado segun busqueda
    def get_queryset(self):
        palabra = self.request.GET.get('busqueda', None)
        usuario = self.request.GET.get('usuario', None)
        object_list = self.model.objects.all()

        if palabra:
            object_list = object_list.filter(
                Q(tema__icontains=palabra ) |
                Q(comentario__icontains=palabra ) 
            )
        if usuario:
            object_list = object_list.filter(
                usuario = usuario
            )        

        object_list = object_list.distinct()

        return object_list

class BitacoraCreateView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'bitacora.add_bitacora'
    model = bitacora
    form_class = bitacoraForm
    success_url= reverse_lazy("bitacora_list")
    success_message = "Entrada creada correctamente"

    def form_valid(self, form):        
        form.instance.usuario = self.request.user
        return super(BitacoraCreateView, self).form_valid(form)

class BitacoraUpdateView(PermissionRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'bitacora.change_bitacora'
    model = bitacora
    form_class = bitacoraForm    
    success_url= reverse_lazy("bitacora_list")
    success_message = "Entrada actualizada correctamente"

    def test_func(self):
        # Obtiene el objeto actual
        objeto = self.get_object()
        # Comprueba si el usuario actual es el creador del objeto o un superusuario
        return self.request.user == objeto.usuario or self.request.user.is_superuser

class BitacoraDetailView(PermissionRequiredMixin,DetailView):
    permission_required = 'bitacora.view_bitacora'
    model = bitacora

class BitacoraDeleteView(PermissionRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,DeleteView):
    permission_required = 'bitacora.delete_bitacora'
    model = bitacora
    success_url= reverse_lazy("bitacora_list")
    success_message = "Entrada eliminada correctamente"

    def test_func(self):
        # Obtiene el objeto actual
        objeto = self.get_object()
        # Comprueba si el usuario actual es el creador del objeto o un superusuario
        return self.request.user == objeto.usuario or self.request.user.is_superuser

        
    #-------------------------------------------------------------- USUARIOS PERFIL

from django.contrib.auth.models import User
from .forms import UserProfileForm

class EditProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('bitacora_list')  # Redirige a la página de perfil después de la edición

    def get_object(self, queryset=None):
        return self.request.user