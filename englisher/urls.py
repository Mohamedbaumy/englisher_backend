from django.urls import path
from .views import home, about_founder, team, dashboard, about_englisher

urlpatterns = [
    path("", home, name="home"),
    path("founder/", about_founder, name="about_founder"),
    path("englisher/", about_englisher, name="about_englisher"),
    path("team/", team, name="team"),
    path("dashboard/", dashboard, name="dashboard"),
]