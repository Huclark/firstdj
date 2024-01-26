from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# create a class that will inherit from forms
class NewTaskForm(forms.Form):
    """This class inherits from Form. Inside the class,
    define all of the fields you want this form to have, thus, all
    of the inputs you will like the user to provide
    """
    # CharField means we'd like the user to input characters
    task = forms.CharField(label="New Task")
    # This is just an additionional input field to
    # make the user add the priority of the to do list
    # minvalue and maxvalue is client-side validation
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# create a global variable of a list of tasks
# tasks = ["foo", "bar", "baz"]
# but this empty list has a problem because it is a global variable so each user will
# end up having access to the lists of others so we will comment it out and
# create it under the index method.
# tasks = []



# Create your views here.
def index(request):
    # take session as a big dictionary representing all the data we have in file about the user
    # here we are going to say that if the session is empty then create an empty list
    # so that we dont end up showing the tasks of another user
    if "tasks" not in request.session:
        # create an empty list
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        # "tasks": tasks ==> this was there when we used tasks as a global variable but
        # since we are not rendering it anymore we have to comment it out and render session instead
        "tasks": request.session["tasks"]
    })
  
def add(request):
    """this takes new tasks without having a fixed list
    """
    # This is server-side validation
    if request.method == "POST":  # If the client is posting/submitting a form
        # Calling NewTaskForm() without an arg just creates an empty form
        # But when you pass in a value to it, it fills the form
        # In this case we are filling the form with POST, thus the user's input
        form = NewTaskForm(request.POST)
        # Now we need to check if the for is valid by calling the is_valid() method
        if form.is_valid():
            # cleaned_data gives you all of the data the user submitted
            # The "task" is the variable which is in the NewTaskForm class
            task = form.cleaned_data["task"]
            # Add the task to the list of tasks because it is valid
            # tasks.append(task) ==> this was used when we created our very own list
            # but now we have to add the new list to the end of our existing list in session
            request.session["tasks"] += [task]
            # Redirect user back to the tasks homepage
            return HttpResponseRedirect(reverse("tasks:index"))
        else: # form is not valid
            # return the add.html file to them again
            # but instead of providing a new form to them,
            # send the existing form data back to them
            # so we can display information about any errors
            # that might have come up as well
            return render(request, "tasks/add.html", {
                "form": form
            })
        
    return render(request, "tasks/add.html", {
        # create a variable form which will just be an instance of NewTaskForm
        "form": NewTaskForm()
    })
