from django.contrib import admin
from Agenda.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ('titulo', 'usuario', )
admin.site.register(Evento, EventoAdmin)

