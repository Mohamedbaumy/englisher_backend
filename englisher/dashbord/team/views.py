from englisher.models import Team


from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy


class TeamMixin(LoginRequiredMixin,
                    PermissionRequiredMixin):
    model = Team
    fields = "__all__"


class GetSuccessUrlOverrideTeamMixin:
    def get_success_url(self):
        return reverse_lazy("team-list")


class TeamListView(TeamMixin, ListView):
    template_name = "dashboard/dash_template/team/list.html"
    permission_required = "englisher.view_team"


class TeamCreateView(TeamMixin,
                         GetSuccessUrlOverrideTeamMixin,
                         CreateView):
    template_name = "dashboard/dash_template/team/form.html"
    permission_required = "englisher.add_team"


class TeamUpdateView(TeamMixin,
                         GetSuccessUrlOverrideTeamMixin,
                         UpdateView):
    template_name = "dashboard/dash_template/team/form.html"
    permission_required = "englisher.change_team"


class TeamDeleteView(TeamMixin,
                         GetSuccessUrlOverrideTeamMixin,
                         DeleteView):
    permission_required = "englisher.delete_team"