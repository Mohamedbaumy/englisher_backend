from django.urls import path
from .views import home, about_founder, team, dashboard

urlpatterns = [
    path("", home, name="home"),
    path("founder/", about_founder, name="about_founder"),
    path("team/", team, name="team"),
    path("dashboard/", dashboard, name="dashboard"),
]