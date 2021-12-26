from englisher.models import Email


from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy


class EmailMixin(LoginRequiredMixin,
                    PermissionRequiredMixin):
    model = Email
    fields = "__all__"


class GetSuccessUrlOverrideEmailMixin:
    def get_success_url(self):
        return reverse_lazy("email-list")


class EmailListView(EmailMixin, ListView):
    template_name = "dashboard/dash_template/email/list.html"
    permission_required = "englisher.view_email"


class EmailCreateView(EmailMixin,
                         GetSuccessUrlOverrideEmailMixin,
                         CreateView):
    template_name = "dashboard/dash_template/email/form.html"
    permission_required = "englisher.add_email"


class EmailUpdateView(EmailMixin,
                         GetSuccessUrlOverrideEmailMixin,
                         UpdateView):
    template_name = "dashboard/dash_template/email/form.html"
    permission_required = "englisher.change_email"


class EmailDeleteView(EmailMixin,
                         GetSuccessUrlOverrideEmailMixin,
                         DeleteView):
    permission_required = "englisher.delete_email"