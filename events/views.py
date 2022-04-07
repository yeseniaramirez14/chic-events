from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.shortcuts import render   

from events.models import Event
from events.forms import BookRequestForm, ContactForm


# Create your views here.
class HomeListView(ListView):
    model = Event
    template_name = "events/home.html"
    context_object_name = "home_list"


class AboutListView(ListView):
    model = Event
    template_name = "events/about.html"
    context_object_name = "about"


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "events/packages.html"
    context_object_name = "event_list"


class ContactUsListView(ListView):
    model = Event
    template_name = "events/contact.html"
    context_object_name = "contact_us"



class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = "events/detail.html"
    context_object_name = "event_detail"



#### Contact Us Page

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True

    else: 
        form = ContactForm()

    return render(
        request, 
        'events/contact.html', 
        {'form': form, 'submitted': submitted}
    )


#### Book Request Page 

def book_request(request):
    submitted = False
    if request.method == 'POST':
        form = BookRequestForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = BookRequestForm()

    return render(
        request, 
        'events/book.html',
        {'form': form, 'submitted': submitted}
    )
