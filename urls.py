from django.urls import path
from . import views

urlpatterns = [
    path("", views.game),
    path("save-score/", views.update_score),
]
