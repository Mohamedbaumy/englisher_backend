from django.urls import path
from .views import (PricingListView,
                    PricingCreateView,
                    PricingUpdateView,
                    PricingDeleteView)


urlpatterns = [
     path("pricing/list/", PricingListView.as_view(), name="pricing-list"),
     path("pricing/create/",
          PricingCreateView.as_view(),
          name="pricing-create"),
     path("pricing/edit/<pk>/",
          PricingUpdateView.as_view(),
          name="pricing-edit"),
     path("pricing/delete/<pk>/",
          PricingDeleteView.as_view(),
          name="pricing-delete"),
]
