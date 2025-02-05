from rest_framework import serializers
from .models import Evento, Participante, Inscricao
from .validators import *


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'  # [')id', 'titulo', 'descricao', 'local', 'data_evento', 'capacidade']


class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = '__all__'

    def validate(self, dados):
        if nome_invalido(dados.get("nome", "")):
            raise serializers.ValidationError(
                {"nome": "O nome deve ter pelo menos 3 caracteres e conter apenas letras"})
        if email_invalido(dados.get('email', "")):
            raise serializers.ValidationError({"email": "O e_mail deve ser válido"})
        if telefone_invalido(dados.get("telefone", "")):
            raise serializers.ValidationError({"telefone": "Número de telefone inválido"})
        if cpf_invalido(str(dados.get("cpf", ""))):
            raise serializers.ValidationError({"cpf": "Número de cpf é inválido"})
        return dados


class InscricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscricao
        fields = '__all__'


# listando inscriçoes por participantes - mostra o evento que o participante se inscreveru
class ListaIncricoesParticipantesSerializer(serializers.ModelSerializer):
    evento = serializers.ReadOnlyField(source='evento.titulo')

    class Meta:
        model = Inscricao
        fields = ['evento', 'data_inscricao']


# listando inscriçoes por evento - mostra a informação do participante por evento
class ListaInscricoesEventoSerializer(serializers.ModelSerializer):
    participante = serializers.ReadOnlyField(source='participante.nome')

    class Meta:
        model = Inscricao
        fields = ['participante', 'data_inscricao']
