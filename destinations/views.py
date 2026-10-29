from django.shortcuts import render, get_object_or_404
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


def destination_detail(request, slug):
    """
    Display the details for a single destination.
    """
    destination = get_object_or_404(Destination, slug=slug)

    return render(
        request,
        "destinations/destination_detail.html",
        {"destination": destination}
    )
