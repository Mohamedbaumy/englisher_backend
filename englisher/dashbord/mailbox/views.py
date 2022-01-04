from englisher.models import Mail, Email
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from englisher.forms import MailForm

from django.urls import reverse_lazy
from englisher.tasks import send_email


class MailMixin(LoginRequiredMixin,
                PermissionRequiredMixin):
    model = Mail
    fields = "__all__"


class GetSuccessUrlOverrideMailMixin:
    def get_success_url(self):
        return reverse_lazy("mail-list")


class GetContextDataOverrideMailMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mail_form"] = MailForm()
        return context


class FormValidOverrideMixin:
    def form_valid(self, form):
        cd = form.cleaned_data
        subject = cd['subject']
        body = cd['body']
        send_email.delay(subject, body)
        return super().form_valid(form)


class MailListView(MailMixin,
                   GetContextDataOverrideMailMixin,
                   ListView):
    template_name = "dashboard/dash_template/mail/list.html"
    permission_required = "englisher.view_mail"


class MailCreateView(MailMixin,
                     FormValidOverrideMixin,
                     GetSuccessUrlOverrideMailMixin,
                     CreateView):
    template_name = "dashboard/dash_template/mail/form.html"
    permission_required = "englisher.add_mail"


class MailDeleteView(MailMixin,
                     GetSuccessUrlOverrideMailMixin,
                     DeleteView):
    permission_required = "englisher.delete_mail"