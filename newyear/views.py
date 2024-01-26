from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request, "newyear/index.html", {
        "newyear": "YES" if datetime.now().month == 1 and datetime.now().day == 1 else "NO"
    })
