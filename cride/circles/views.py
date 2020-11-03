"""Circle views."""

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Serializers
from cride.circles.serializers import CircleSerializer, CreateCircleSerializer

# models
from cride.circles.models import Circle

@api_view(['GET'])
def list_circles(request):
    """List circles."""

    circles = Circle.objects.filter(is_public=True)
    serializer = CircleSerializer(circles, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def create_circles(request):
    """Create Circle""" 
    serializer = CreateCircleSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)