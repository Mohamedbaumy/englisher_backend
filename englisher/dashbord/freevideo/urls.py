from django.urls import path
from .views import (FreeVideoListView,
                    FreeVideoCreateView,
                    FreeVideoUpdateView,
                    FreeVideoDeleteView)


urlpatterns = [
     path("freevideo/list/", FreeVideoListView.as_view(), name="freevideo-list"),
     path("freevideo/create/",
          FreeVideoCreateView.as_view(),
          name="freevideo-create"),
     path("freevideo/edit/<pk>/",
          FreeVideoUpdateView.as_view(),
          name="freevideo-edit"),
     path("freevideo/delete/<pk>/",
          FreeVideoDeleteView.as_view(),
          name="freevideo-delete"),
]
