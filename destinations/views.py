from django.shortcuts import render, get_object_or_404
from .models import Destination, Place


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

def place_detail(request, destination_slug, place_slug):
    """
    Display the details for a single place within a destination.
    """
    place = get_object_or_404(
        Place,
        destination__slug=destination_slug,
        slug=place_slug
    )

    return render(
        request,
        "destinations/place_detail.html",
        {"place": place}
    )
