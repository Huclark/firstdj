from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    """Returns 'Hello, world!' to the client

    Args: request (link): The HTTP request that the user made
    in order to access our web server

    Returns:
    	str: Returns the string, 'Hello, world!'
	"""
    # return HttpResponse("Hello, world!")
    return render(request, "hello/index.html")

def huclark(request):
    """Returns 'Hello, Huclark!' to the client

    Args:
        request (http): The HTTP request that the user made
        in order to access our web server

    Returns:
        str: Returns the string, 'Hello, world!'
    """
    return HttpResponse("Hello, Huclark!")

def surname(request):
    """Returns 'Hello, Vanderpuye!' to the client

    Args:
        request (http): The HTTP request that the user made
        in order to access our web server

    Returns:
        str: Returns the string, 'Hello, world!'
    """
    return HttpResponse("Hello, Vanderpuye!")

def greet(request, name):
    """Greets the user with whatever name the user provides

    Args:
        request (http): http request
        name (str): name to address

    Returns:
        str: greetings
    """
    # return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
