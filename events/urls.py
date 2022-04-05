from django.urls import path

from events.views import (
    EventDetailView,
    EventListView,
    HomeListView,
    ContactUsListView,
    BookNowCreateView,
    SuccessListView,
    AboutListView
)

urlpatterns = [
    path("services/", EventListView.as_view(), name="list_services"),
    path("events/<int:pk>/", EventDetailView.as_view(), name="show_event"),
    path("", HomeListView.as_view(), name="home"),
    path("about/", AboutListView.as_view(), name="about"),
    path("contactus/", ContactUsListView.as_view(), name="contact_us"),
    path("book-now/", BookNowCreateView.as_view(), name="book_now"),
    path("booked/", SuccessListView.as_view(), name="successful_booking"),


]
