from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from events.models import Event


# Create your views here.
class HomeListView(ListView):
    model = Event
    template_name = "events/home.html"
    context_object_name = "home_list"

    def get_queryset(self):
        return Event.objects.filter(members=self.request.user)

class AboutListView(ListView):
    model = Event
    template_name = "events/about.html"
    context_object_name = "about"

    def get_queryset(self):
        return Event.objects.filter(members=self.request.user)

class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "events/list.html"
    context_object_name = "event_list"

    def get_queryset(self):
        return Event.objects.filter(members=self.request.user)

class ContactUsListView(ListView):
    model = Event
    template_name = "events/contact.html"
    context_object_name = "contact_us"

    def get_queryset(self):
        return Event.objects.filter(members=self.request.user)

class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = "events/detail.html"
    context_object_name = "event_detail"


class BookNowCreateView(CreateView):
    model = Event
    template_name = "events/book.html"
    fields = ["name", "description", "members"]
    context_object_name = "book_now"

    def get_success_url(self):
        return reverse_lazy("successful_booking", args=[self.object.id])

class SuccessListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "events/success.html"
    context_object_name = "successful_booking"

    def get_queryset(self):
        return Event.objects.filter(members=self.request.user)