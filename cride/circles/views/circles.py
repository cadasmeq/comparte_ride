"""Circles Views"""

# Django REST Framework
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Models
from cride.circles.models import Circle

# Serializers
from cride.circles.serializers import (
    CircleSerializer,
    CreateCircleSerializer
)

class CirclesViewSet(viewsets.ViewSet):
    """Circles ViewSet"""

    def list(self, request):
        queryset = Circle.objects.all()
        serializer = CircleSerializer(queryset, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def list_circles(request):
    """List circles."""
    circles = Circle.objects.filter(is_public=True)
    serializer = CircleSerializer(circles, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_circle(request):
    """Create circle."""
    serializer = CreateCircleSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    circle = serializer.save()
    return Response(CircleSerializer(circle).data)
