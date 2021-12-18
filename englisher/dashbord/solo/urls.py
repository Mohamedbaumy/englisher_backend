from django.urls import path
from .views import (SiteUpdateView, AboutUpdateView)


urlpatterns = [
     path("site/edit/<pk>/",
          SiteUpdateView.as_view(),
          name="site-edit"),
     path("about/edit/<pk>/",
          AboutUpdateView.as_view(),
          name="about-edit"),
]
