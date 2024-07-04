from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("pesquisar", views.pesquisar admin.site.urls),
    path("admin/", include('loja.url')admin.site.urls),
]
