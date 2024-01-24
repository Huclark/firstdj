from django.urls import path
from . import views

# create a list of all the allowable urls that can be
# accessed for this particular app
urlpatterns = [
    # default route represented by the empty string
    path("", views.index, name="index"),
    # this path loads the greet function
    path("<str:name>", views.greet, name="greet"),
    # this path loads huclark function
    path("huclark", views.huclark, name="huclark"),
    # this path loads the surname function
    path("surname", views.surname, name="vanderpuye"),  
]
