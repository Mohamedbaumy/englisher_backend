from django.urls import path
from .views import (TestimonialsListView,
                    TestimonialsCreateView,
                    TestimonialsUpdateView,
                    TestimonialsDeleteView)


urlpatterns = [
     path("testimonials/list/", TestimonialsListView.as_view(), name="testimonials-list"),
     path("testimonials/create/",
          TestimonialsCreateView.as_view(),
          name="testimonials-create"),
     path("testimonials/edit/<pk>/",
          TestimonialsUpdateView.as_view(),
          name="testimonials-edit"),
     path("testimonials/delete/<pk>/",
          TestimonialsDeleteView.as_view(),
          name="testimonials-delete"),
]
