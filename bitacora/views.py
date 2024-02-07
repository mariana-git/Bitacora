from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy

from .forms import *
from .models import *

class BitacoraListView(PermissionRequiredMixin,ListView):
    permission_required = 'bitacora.view_bitacora'
    model = bitacora
    paginate_by = 5

     # en caso de que la url tenga un usuario especifico, inicializo la tabla con el servicio elegido
    # def get_queryset(self):
    #     if self.request.GET.get('tipo') is not None:
    #         return bitacora.objects.filter(
    #             tipo__icontains = self.request.GET['tipo']
    #         )

    #     return super().get_queryset()

class BitacoraCreateView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'bitacora.add_bitacora'
    model = bitacora
    form_class = bitacoraForm
    success_url= reverse_lazy("bitacora_list")
    success_message = "Entrada creada correctamente"

    def form_valid(self, form):        
        form.instance.usuario = self.request.user
        return super(BitacoraCreateView, self).form_valid(form)

class BitacoraUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'bitacora.change_bitacora'
    model = bitacora
    form_class = bitacoraForm    
    success_url= reverse_lazy("bitacora_list")
    success_message = "Entrada actualizada correctamente"

class BitacoraDetailView(PermissionRequiredMixin,DetailView):
    permission_required = 'bitacora.view_bitacora'
    model = bitacora

class BitacoraDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    permission_required = 'bitacora.delete_bitacora'
    model = bitacora
    success_url= reverse_lazy("bitacora_list")
    success_message = "Entrada eliminada correctamente"


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