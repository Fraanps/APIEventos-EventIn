from rest_framework import viewsets, generics
from rest_framework.views import APIView

from .models import Evento, Participante, Inscricao
from .serializers import *
    # EventoSerializer, ParticipanteSerializer, InscricaoSerializer, ListaInscricoesEventoSerializer, ListaIncricoesParticipantesSerializer)


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer

class InscricaoViewSet(viewsets.ModelViewSet):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer

class ListaInscricoesParticipantesViewSet(generics.ListAPIView):
    serializer_class = ListaIncricoesParticipantesSerializer
    def get_queryset(self):
        participante_id = self.kwargs['pk']
        return Inscricao.objects.filter(participante_id=participante_id)

class ListaInscricoesEventosViewSet(generics.ListAPIView):
    serializer_class = ListaInscricoesEventoSerializer
    def get_queryset(self):
        evento_id = self.kwargs['pk']
        return Inscricao.objects.filter(evento_id=evento_id)


