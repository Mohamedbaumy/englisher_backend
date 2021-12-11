from django.urls import path
from .views import (FoundrFeatureListView,
                    FoundrFeatureCreateView,
                    FoundrFeatureUpdateView,
                    FoundrFeatureDeleteView)


urlpatterns = [
     path("foundrfeature/list/", FoundrFeatureListView.as_view(), name="foundrfeature-list"),
     path("foundrfeature/create/",
          FoundrFeatureCreateView.as_view(),
          name="foundrfeature-create"),
     path("foundrfeature/edit/<pk>/",
          FoundrFeatureUpdateView.as_view(),
          name="foundrfeature-edit"),
     path("foundrfeature/delete/<pk>/",
          FoundrFeatureDeleteView.as_view(),
          name="foundrfeature-delete"),
]
