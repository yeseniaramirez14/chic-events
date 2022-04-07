from django.urls import path

from events.views import (
    EventDetailView,
    EventListView,
    HomeListView,
    AboutListView,
    book_request,
    contact
)


urlpatterns = [
    path("packages/", EventListView.as_view(), name="list_packages"),
    path("events/<int:pk>/", EventDetailView.as_view(), name="show_event"),
    path("", HomeListView.as_view(), name="home"),
    path("about/", AboutListView.as_view(), name="about"),
    path("contactus/", contact, name="contact_us"),
    path("book-now/", book_request, name="book_now"),

]
