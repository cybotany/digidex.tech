from rest_framework import viewsets, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from wagtail.api.v2.views import PagesAPIViewSet

from .models import UserInventory
from .serializers import UserInventorySerializer


class UserInventoryAPIViewSet(PagesAPIViewSet):
    model = UserInventory
    base_serializer_class = UserInventorySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    lookup_field = 'uuid'
    body_fields = ['uuid', 'slug', 'title', 'description', 'url']
    meta_fields = ['uuid']