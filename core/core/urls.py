from django.contrib import admin
from django.urls import path
from LinguasLivres import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("traduzir/", views.traduzir_view),
]