from django.urls import path
from .views import (MailListView,
                    MailCreateView,
                    MailDeleteView)


urlpatterns = [
     path("mail/list/", MailListView.as_view(), name="mail-list"),
     path("mail/create/",
          MailCreateView.as_view(),
          name="mail-create"),
     path("mail/delete/<pk>/",
          MailDeleteView.as_view(),
          name="mail-delete"),
]
