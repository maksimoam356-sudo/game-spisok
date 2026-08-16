from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from game.views import home, gamedetail

urlpatterns = [
    path("",home),
    path('gamedetail/<int:game_id>/',gamedetail)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

