from eventin.views import participantes
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('participantes', participantes),
]
