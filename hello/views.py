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
    return HttpResponse("Hello, world!")
