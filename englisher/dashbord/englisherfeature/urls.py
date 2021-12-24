from django.urls import path
from .views import (EnglisherFeatureListView,
                    EnglisherFeatureCreateView,
                    EnglisherFeatureUpdateView,
                    EnglisherFeatureDeleteView)


urlpatterns = [
     path("englisherfeature/list/", EnglisherFeatureListView.as_view(), name="englisherfeature-list"),
     path("englisherfeature/create/",
          EnglisherFeatureCreateView.as_view(),
          name="englisherfeature-create"),
     path("englisherfeature/edit/<pk>/",
          EnglisherFeatureUpdateView.as_view(),
          name="englisherfeature-edit"),
     path("englisherfeature/delete/<pk>/",
          EnglisherFeatureDeleteView.as_view(),
          name="englisherfeature-delete"),
]
