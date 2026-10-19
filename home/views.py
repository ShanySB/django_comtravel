from django.shortcuts import render


def home(request):
    """
    Displays ComTravel home page
    """
    return render(request, "home/index.html")
