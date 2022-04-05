from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from events.models import Event

from tasks.models import Task


# Create your views here.
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "event", "assignee"]

    def get_success_url(self):
        return reverse_lazy("show_event", args=[self.object.event_id])


class TaskListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "tasks/list.html"
    context_object_name = "list_of_tasks"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["is_completed"]
    success_url = reverse_lazy("show_my_tasks")
