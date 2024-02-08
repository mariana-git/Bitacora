from django.contrib import admin
from .models import bitacora
from django.contrib.admin.models import LogEntry

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'action_time', 'user', 'content_type', 'object_id', 'action_flag']
    search_fields = ['user__username', 'object_repr']
    list_filter = ['action_flag', 'content_type']

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(LogEntry, LogEntryAdmin)

admin.site.register(bitacora)


