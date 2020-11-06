"""Circles Views"""

# Django REST Framework
from rest_framework import viewsets
from rest_framework.response import Response

# Models
from cride.circles.models import Circle

# Serializers
from cride.circles.serializers import CircleModelSerializer

class CirclesViewSet(viewsets.ModelViewSet):
    """Circles ViewSet"""

    queryset = Circle.objects.all()
    serializer_class = CircleModelSerializer

