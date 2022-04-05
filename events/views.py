from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from events.models import Event


# Create your views here.
class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "events/list.html"
    context_object_name = "event_list"

    def get_queryset(self):
        return Event.objects.filter(members=self.request.user)


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = "events/detail.html"
    context_object_name = "event_detail"


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    template_name = "events/create.html"
    fields = ["name", "description", "members"]
    context_object_name = "event_create"

    def get_success_url(self):
        return reverse_lazy("show_event", args=[self.object.id])
