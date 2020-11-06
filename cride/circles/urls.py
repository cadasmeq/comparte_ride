"""Circles URLs."""

# Django
from django.urls import path

# Views
from cride.circles.views import CirclesViewSet, create_circle

urlpatterns = [
    path('circles/', CirclesViewSet.as_view({'get':'list'})),
    path('circles/create/', create_circle)
]
