from rest_framework import viewsets, generics, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Evento, Participante, Inscricao
from .serializers import *


class EventoViewSet(viewsets.ModelViewSet):
    # autenticação
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    # filtro e ordenação
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ["titulo"]
    search_fields = ["titulo", "local"]

class ParticipanteViewSet(viewsets.ModelViewSet):
    # autenticação
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Participante.objects.all()
    # serializer_class = ParticipanteSerializer
    # filtro e ordenação
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ["nome"]
    search_fields = ["nome", "cpf"]

    # definindo a versão que será chamada
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return ParticipanteSerializerV2
        return ParticipanteSerializer


class InscricaoViewSet(viewsets.ModelViewSet):
    # autenticação
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser] # só acessa se o usuário for admin
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


