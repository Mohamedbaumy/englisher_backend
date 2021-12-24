from englisher.models import EnglisherFeature


from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy


class EnglisherFeatureMixin(LoginRequiredMixin,
                    PermissionRequiredMixin):
    model = EnglisherFeature
    fields = "__all__"


class GetSuccessUrlOverrideEnglisherFeatureMixin:
    def get_success_url(self):
        return reverse_lazy("englisherfeature-list")


class EnglisherFeatureListView(EnglisherFeatureMixin, ListView):
    template_name = "dashboard/dash_template/englisherfeature/list.html"
    permission_required = "englisher.view_englisherfeature"


class EnglisherFeatureCreateView(EnglisherFeatureMixin,
                         GetSuccessUrlOverrideEnglisherFeatureMixin,
                         CreateView):
    template_name = "dashboard/dash_template/englisherfeature/form.html"
    permission_required = "englisher.add_englisherfeature"


class EnglisherFeatureUpdateView(EnglisherFeatureMixin,
                         GetSuccessUrlOverrideEnglisherFeatureMixin,
                         UpdateView):
    template_name = "dashboard/dash_template/englisherfeature/form.html"
    permission_required = "englisher.change_freeVideo"


class EnglisherFeatureDeleteView(EnglisherFeatureMixin,
                         GetSuccessUrlOverrideEnglisherFeatureMixin,
                         DeleteView):
    permission_required = "englisher.delete_englisherfeature"