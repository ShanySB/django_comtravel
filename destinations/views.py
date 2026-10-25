from django.shortcuts import render
from .models import Destination


def destination_list(request):
    """
    Display a list of all available destinations.
    """
    destinations = Destination.objects.all()

    return render(
        request,
        "destinations/destination_list.html",
        {"destinations": destinations}
    )