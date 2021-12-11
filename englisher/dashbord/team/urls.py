from django.urls import path
from .views import (TeamListView,
                    TeamCreateView,
                    TeamUpdateView,
                    TeamDeleteView)


urlpatterns = [
     path("team/list/", TeamListView.as_view(), name="team-list"),
     path("team/create/",
          TeamCreateView.as_view(),
          name="team-create"),
     path("team/edit/<pk>/",
          TeamUpdateView.as_view(),
          name="team-edit"),
     path("team/delete/<pk>/",
          TeamDeleteView.as_view(),
          name="team-delete"),
]
