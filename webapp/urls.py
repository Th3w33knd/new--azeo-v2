from django.urls import path
from . import views


urlpatterns = [
    path("", views.homepage, name="home"),
    path("team/", views.team, name="team"),
    path("azeoid/", views.azeoid_register, name="azeoid"),
]
