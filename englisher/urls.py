from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("founder/", views.about_founder, name="about_founder"),
    path("englisher/", views.about_englisher, name="about_englisher"),
    path("team/", views.team, name="team"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("test", views.add_email , name="test-url"),
]
