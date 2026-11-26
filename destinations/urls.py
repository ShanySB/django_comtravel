from django.urls import path
from . import views

app_name = 'destinations'

urlpatterns = [
    path('', views.destination_list, name='destination_list'),
    path('<slug:slug>/', views.destination_detail, name='destination_detail'),
    path(
        '<slug:destination_slug>/<slug:place_slug>/',
        views.place_detail,
        name='place_detail'
    ),
]
