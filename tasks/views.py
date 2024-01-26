from django.shortcuts import render

# create a global variable of a list of tasks
tasks = ["foo", "bar", "baz"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
    
def add(request):
    """this takes new tasks without having a fixed list
    """
    return render(request, "tasks/add.html")
