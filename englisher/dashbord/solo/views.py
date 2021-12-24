from englisher.models import SiteConfiguration,AboutFounder, AboutEnglisher


from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.views.generic.edit import UpdateView

from django.urls import reverse_lazy


class SiteMixin(LoginRequiredMixin,
                    PermissionRequiredMixin):
    model = SiteConfiguration
    fields = "__all__"


class GetSuccessUrlOverrideSiteMixin:
    def get_success_url(self):
        return reverse_lazy("dashboard")


class SiteUpdateView(SiteMixin,
                         GetSuccessUrlOverrideSiteMixin,
                         UpdateView):
    template_name = "dashboard/dash_template/site_config/form.html"
    permission_required = "englisher.change_siteconfiguration"


class AboutMixin(LoginRequiredMixin,
                    PermissionRequiredMixin):
    model = AboutFounder
    fields = "__all__"


class GetSuccessUrlOverrideAboutMixin:
    def get_success_url(self):
        return reverse_lazy("dashboard")


class AboutUpdateView(AboutMixin,
                         GetSuccessUrlOverrideAboutMixin,
                         UpdateView):
    template_name = "dashboard/dash_template/about_config/form.html"
    permission_required = "englisher.change_aboutfounder"


class AboutEnglisherMixin(LoginRequiredMixin,
                    PermissionRequiredMixin):
    model = AboutEnglisher
    fields = "__all__"


class GetSuccessUrlOverrideAboutEnglisherMixin:
    def get_success_url(self):
        return reverse_lazy("dashboard")


class AboutEnglisherUpdateView(AboutEnglisherMixin,
                         GetSuccessUrlOverrideAboutEnglisherMixin,
                         UpdateView):
    template_name = "dashboard/dash_template/about_englisher/form.html"
    permission_required = "englisher.change_aboutenglisher"
