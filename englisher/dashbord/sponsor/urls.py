from django.urls import path
from .views import (SponsorListView,
                    SponsorCreateView,
                    SponsorUpdateView,
                    SponsorDeleteView)


urlpatterns = [
     path("sponsor/list/", SponsorListView.as_view(), name="sponsor-list"),
     path("sponsor/create/",
          SponsorCreateView.as_view(),
          name="sponsor-create"),
     path("sponsor/edit/<pk>/",
          SponsorUpdateView.as_view(),
          name="sponsor-edit"),
     path("sponsor/delete/<pk>/",
          SponsorDeleteView.as_view(),
          name="sponsor-delete"),
]
