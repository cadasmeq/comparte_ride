"""Circle URLs."""

# django
from django.urls import path

# views
from cride.circles.views import list_circles, create_circles

urlpatterns = [
    path('circles/', list_circles),
    path('circles/create/', create_circles)
]
