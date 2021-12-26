from django.urls import path
from .views import (EmailListView,
                    EmailCreateView,
                    EmailUpdateView,
                    EmailDeleteView)


urlpatterns = [
     path("email/list/", EmailListView.as_view(), name="email-list"),
     path("email/create/",
          EmailCreateView.as_view(),
          name="email-create"),
     path("email/edit/<pk>/",
          EmailUpdateView.as_view(),
          name="email-edit"),
     path("email/delete/<pk>/",
          EmailDeleteView.as_view(),
          name="email-delete"),
]
