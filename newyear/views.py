from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, "newyear/index.html", {
        "newyear": "YES" if datetime.now().month == 1 and datetime.now().day == 1 else "NO"
    })
