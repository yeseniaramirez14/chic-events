from django.urls import path

from events.views import (
    EventCreateView,
    EventDetailView,
    EventListView,
)

urlpatterns = [
    path("", EventListView.as_view(), name="list_events"),
    path("<int:pk>/", EventDetailView.as_view(), name="show_event"),
    path("create/", EventCreateView.as_view(), name="create_event"),
]
