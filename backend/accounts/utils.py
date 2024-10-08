from django.db import transaction
from django.contrib.auth.models import Group

from base.utils import assign_group_permissions, assign_wagtail_group_permissions


@transaction.atomic
def setup_new_trainer(user):
    # Assign user permissions
    assign_user_permissions(user)
    # Assign trainer permissions
    assign_trainer_permissions(user)
    # Setup inventory boxes for the new user
    from inventory.utils import setup_inventory_boxes
    setup_inventory_boxes(user)


def assign_user_permissions(user):
    from inventory.constants import PAGE_PERMISSIONS, COLLECTION_PERMISSIONS

    group = user.get_group()
    assign_trainer_permissions(user)
    
    page = user.get_page()
    assign_wagtail_group_permissions(group, page, PAGE_PERMISSIONS)
    
    collection = user.get_collection().collection
    assign_wagtail_group_permissions(group, collection, COLLECTION_PERMISSIONS)


def assign_trainer_permissions(user):
    group, created = Group.objects.get_or_create(name='Trainers')
    if created:
        # Assign botany permissions for all trainers
        from botany.constants import BOTANY_PERMISSIONS
        assign_group_permissions(group, BOTANY_PERMISSIONS)

        # Assign ntag permissions for all trainers
        from ntags.constants import NTAG_PERMISSIONS
        assign_group_permissions(group, NTAG_PERMISSIONS)
    user.groups.add(group)
