"""Memberships Serializer"""

# Django REST Framework
from rest_framework import serializers

# Models
from cride.circles.models import Membership

# Models
from cride.users.serializers import UserModelSerializer

class MembershipModelSerializer(serializers.ModelSerializer):
    """MemberModelSerializer."""

    user = UserModelSerializer(read_only=True)
    invited_by = serializers.StringRelatedField()
    joined_at = serializers.DateTimeField(source='created', read_only=True)

    class Meta:
        """Meta Class."""

        model = Membership
        fields = (
            'users',
            'is_admin', 'is_active',
            'used_invitations', 'remaining_invitations',
            'invited_by',
            'rides_taken', 'rides_offered'
            'joined_at'
        )
        read_ony_fields = (
            'user',
            'used_invitations',
            'invited_by',
            'rides_taken', 'rides_offered'
        )


