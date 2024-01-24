from django.urls import path
from . import views

# create a list of all the allowable urls that can be
# accessed for this particular app
urlpatterns = [
    path("", views.index, name="index")
]
