"""Circle views."""

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Serializers
from cride.circles.serializers import CircleSerializer
# Django
from django.http import JsonResponse, HttpResponse

# models
from cride.circles.models import Circle

@api_view(['GET'])
def list_circles(request):
    """List circles."""

    circles = Circle.objects.filter(is_public=True)
    data = []
    for circle in circles:
        serializer = CircleSerializer(circle)
        data.append(serializer.data)

    return Response(data)

@api_view(['POST'])
def create_circles(request):
    """Create Circle"""
    name = request.data['name']
    slug_name = request.data['slug_name']
    about = request.data.get('about', '')
    circle = Circle.objects.create(
        name=name, 
        slug_name=slug_name, 
        about=about
    )
    data = {
        'name': circle.name,
        'slug_name': circle.slug_name,
        'rides_take': circle.rides_offered,
        'members_limit': circle.members_limit
    }
    return Response(data)