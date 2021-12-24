from django.urls import path
from .views import (SiteUpdateView, AboutUpdateView, AboutEnglisherUpdateView)


urlpatterns = [
     path("site/edit/<pk>/",
          SiteUpdateView.as_view(),
          name="site-edit"),
     path("about/edit/<pk>/",
          AboutUpdateView.as_view(),
          name="about-edit"),
     path("about_englisher/edit/<pk>/",
          AboutEnglisherUpdateView.as_view(),
          name="about-englisher-edit"),
]
