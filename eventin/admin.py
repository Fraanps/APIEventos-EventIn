from django.contrib import admin
from .models import Evento, Participante, Inscricao


class EventosAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'local', 'data_evento', 'capacidade')
    list_display_links = ('id', 'titulo')
    list_per_page = 20 # paginação
    search_fields = ('titulo', 'local')

admin.site.register(Evento, EventosAdmin)

class ParticipantesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email', 'telefone')
    list_display_links = ('id', 'nome')
    list_per_page = 20
    search_fields = ('titulo', 'local')

admin.site.register(Participante, ParticipantesAdmin)

class InscricoesAdmin(admin.ModelAdmin):
    list_display = ('id', 'evento', 'participante', 'data_inscricao')
    list_display_links = ('id',)
    list_per_page = 20
    search_fields = ('evento', 'participante')

admin.site.register(Inscricao, InscricoesAdmin)