from englisher.models import Pricing


from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy


class PricingMixin(LoginRequiredMixin,
                    PermissionRequiredMixin):
    model = Pricing
    fields = "__all__"


class GetSuccessUrlOverridePricingMixin:
    def get_success_url(self):
        return reverse_lazy("pricing-list")


class PricingListView(PricingMixin, ListView):
    template_name = "dashboard/dash_template/pricing/list.html"
    permission_required = "englisher.view_pricing"


class PricingCreateView(PricingMixin,
                         GetSuccessUrlOverridePricingMixin,
                         CreateView):
    template_name = "dashboard/dash_template/pricing/form.html"
    permission_required = "englisher.add_pricing"


class PricingUpdateView(PricingMixin,
                         GetSuccessUrlOverridePricingMixin,
                         UpdateView):
    template_name = "dashboard/dash_template/pricing/form.html"
    permission_required = "englisher.change_pricing"


class PricingDeleteView(PricingMixin,
                         GetSuccessUrlOverridePricingMixin,
                         DeleteView):
    permission_required = "englisher.delete_pricing"