"""Circle Model Admin"""

# Django
from django.contrib import admin

# Models
from cride.circles.models import Circle

@admin.register(Circle)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Model Admin."""

    list_display = (
        'slug_name', 
        'name', 
        'is_public', 
        'is_limited', 
        'members_limit'
    )
    search_fields = (
        'name', 
        'slug_name', 
    )
    list_filter = (
        'verified', 
        'is_public',
        'is_limited'
    )

