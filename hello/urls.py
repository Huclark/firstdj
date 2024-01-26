from django.urls import path
from . import views

# create a list of all the allowable urls that can be
# accessed for this particular app
# the 1st arg of path is the url the client is visiting
# the 2nd arg is what view should be rendered when the url is visited
# the 3rd arg(optional) is just to reference the url so that later
# we can easily reference the url
urlpatterns = [
    # default route represented by the empty string
    # which loads the index function
    path("", views.index, name="index"),
    # this path loads the greet function
    path("<str:name>", views.greet, name="greet"),
    # this path loads huclark function
    path("huclark", views.huclark, name="huclark"),
    # this path loads the surname function
    path("surname", views.surname, name="vanderpuye"),  
]
