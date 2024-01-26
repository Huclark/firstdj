from django.urls import path

from . import views

# add this so as to be more specific when calling routes
app_name = "tasks"
# create the paths
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]
