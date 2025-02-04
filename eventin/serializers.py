from rest_framework import serializers
from .models import Evento, Participante, Inscricao


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__' #[')id', 'titulo', 'descricao', 'local', 'data_evento', 'capacidade']

class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = '__all__'

class InscricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscricao
        fields = '__all__'