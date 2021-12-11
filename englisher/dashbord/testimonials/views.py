from englisher.models import Testimonials


from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy


class TestimonialsMixin(LoginRequiredMixin,
                    PermissionRequiredMixin):
    model = Testimonials
    fields = "__all__"


class GetSuccessUrlOverrideTestimonialsMixin:
    def get_success_url(self):
        return reverse_lazy("testimonials-list")


class TestimonialsListView(TestimonialsMixin, ListView):
    template_name = "dashboard/dash_template/testimonials/list.html"
    permission_required = "englisher.view_testimonials"


class TestimonialsCreateView(TestimonialsMixin,
                         GetSuccessUrlOverrideTestimonialsMixin,
                         CreateView):
    template_name = "dashboard/dash_template/testimonials/form.html"
    permission_required = "englisher.add_testimonials"


class TestimonialsUpdateView(TestimonialsMixin,
                         GetSuccessUrlOverrideTestimonialsMixin,
                         UpdateView):
    template_name = "dashboard/dash_template/testimonials/form.html"
    permission_required = "englisher.change_testimonials"


class TestimonialsDeleteView(TestimonialsMixin,
                         GetSuccessUrlOverrideTestimonialsMixin,
                         DeleteView):
    permission_required = "englisher.delete_testimonials"