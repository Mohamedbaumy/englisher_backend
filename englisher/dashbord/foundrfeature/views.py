from englisher.models import FoundrFeature


from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy


class FoundrFeatureMixin(LoginRequiredMixin,
                    PermissionRequiredMixin):
    model = FoundrFeature
    fields = "__all__"


class GetSuccessUrlOverrideFoundrFeatureMixin:
    def get_success_url(self):
        return reverse_lazy("foundrfeature-list")


class FoundrFeatureListView(FoundrFeatureMixin, ListView):
    template_name = "dashboard/dash_template/foundrfeature/list.html"
    permission_required = "englisher.view_foundrfeature"


class FoundrFeatureCreateView(FoundrFeatureMixin,
                         GetSuccessUrlOverrideFoundrFeatureMixin,
                         CreateView):
    template_name = "dashboard/dash_template/foundrfeature/form.html"
    permission_required = "englisher.add_foundrfeature"


class FoundrFeatureUpdateView(FoundrFeatureMixin,
                         GetSuccessUrlOverrideFoundrFeatureMixin,
                         UpdateView):
    template_name = "dashboard/dash_template/foundrfeature/form.html"
    permission_required = "englisher.change_freeVideo"


class FoundrFeatureDeleteView(FoundrFeatureMixin,
                         GetSuccessUrlOverrideFoundrFeatureMixin,
                         DeleteView):
    permission_required = "englisher.delete_foundrfeature"