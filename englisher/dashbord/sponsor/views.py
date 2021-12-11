from englisher.models import Sponsor


from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy


class SponsorMixin(LoginRequiredMixin,
                    PermissionRequiredMixin):
    model = Sponsor
    fields = "__all__"


class GetSuccessUrlOverrideSponsorMixin:
    def get_success_url(self):
        return reverse_lazy("sponsor-list")


class SponsorListView(SponsorMixin, ListView):
    template_name = "dashboard/dash_template/sponsor/list.html"
    permission_required = "englisher.view_sponsor"


class SponsorCreateView(SponsorMixin,
                         GetSuccessUrlOverrideSponsorMixin,
                         CreateView):
    template_name = "dashboard/dash_template/sponsor/form.html"
    permission_required = "englisher.add_sponsor"


class SponsorUpdateView(SponsorMixin,
                         GetSuccessUrlOverrideSponsorMixin,
                         UpdateView):
    template_name = "dashboard/dash_template/sponsor/form.html"
    permission_required = "englisher.change_sponsor"


class SponsorDeleteView(SponsorMixin,
                         GetSuccessUrlOverrideSponsorMixin,
                         DeleteView):
    permission_required = "englisher.delete_sponsor"