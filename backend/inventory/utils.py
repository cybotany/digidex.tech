from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Permission


def assign_inventory_permissions(group):
    """
    Assigns the necessary inventory permissions for the given group.
    """
    permissions = Permission.objects.filter(
        codename__in=[]
    )
    group.permissions.add(*permissions)
    group.save()
    return group
