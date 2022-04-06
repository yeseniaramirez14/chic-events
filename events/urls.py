from django.urls import path

from events.views import (
    EventDetailView,
    EventListView,
    HomeListView,
    ContactUsListView,
    BookNowCreateView,
    SuccessListView,
    AboutListView,
    ContactSuccessListView,
    contact
)


urlpatterns = [
    path("packages/", EventListView.as_view(), name="list_packages"),
    path("events/<int:pk>/", EventDetailView.as_view(), name="show_event"),
    path("", HomeListView.as_view(), name="home"),
    path("about/", AboutListView.as_view(), name="about"),
    path("contactus/", contact, name="contact_us"),
    path("book-now/", BookNowCreateView.as_view(), name="book_now"),
    path("booked/", SuccessListView.as_view(), name="successful_booking"),
    path("message_sent", ContactSuccessListView.as_view(), name="successful_contact")


]
