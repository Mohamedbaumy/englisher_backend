from englisher.models import FreeVideo


from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy


class FreeVideoMixin(LoginRequiredMixin,
                    PermissionRequiredMixin):
    model = FreeVideo
    fields = "__all__"


class GetSuccessUrlOverrideFreeVideoMixin:
    def get_success_url(self):
        return reverse_lazy("freevideo-list")


class FreeVideoListView(FreeVideoMixin, ListView):
    template_name = "dashboard/dash_template/freevideo/list.html"
    permission_required = "englisher.view_freevideo"


class FreeVideoCreateView(FreeVideoMixin,
                         GetSuccessUrlOverrideFreeVideoMixin,
                         CreateView):
    template_name = "dashboard/dash_template/freevideo/form.html"
    permission_required = "englisher.add_freevideo"


class FreeVideoUpdateView(FreeVideoMixin,
                         GetSuccessUrlOverrideFreeVideoMixin,
                         UpdateView):
    template_name = "dashboard/dash_template/freevideo/form.html"
    permission_required = "englisher.change_freeVideo"


class FreeVideoDeleteView(FreeVideoMixin,
                         GetSuccessUrlOverrideFreeVideoMixin,
                         DeleteView):
    permission_required = "englisher.delete_freevideo"