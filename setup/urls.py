from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers, permissions
from eventin.views import * #EventoViewSet, ParticipanteViewSet, InscricaoViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# configuração do Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Eventin API",
        default_version='v1',
        description="API para cadastro de eventos",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="fran@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('eventos', EventoViewSet, basename='Eventos')
router.register('participantes', ParticipanteViewSet, basename='Participantes')
router.register('inscricoes', InscricaoViewSet, basename='Inscricoes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('participantes/<int:pk>/inscricoes', ListaInscricoesParticipantesViewSet.as_view()),
    path('eventos/<int:pk>/inscricoes', ListaInscricoesEventosViewSet.as_view()),

    # URLs do swagger
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),

]
