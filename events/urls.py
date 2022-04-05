from django.urls import path

from events.views import (
    ProjectCreateView,
    ProjectDetailView,
    ProjectListView,
)

urlpatterns = [
    path("", ProjectListView.as_view(), name="list_projects"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="show_project"),
    path("create/", ProjectCreateView.as_view(), name="create_project"),
]
