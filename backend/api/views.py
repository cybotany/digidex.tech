from rest_framework import routers

from trainers.viewsets import TrainerViewSet
# from accounts.viewsets import UserAssistantDetail
from nearfieldcommunication.viewsets import NFCTagViewSet, NFCTagDesignViewSet
# from biology.viewsets import UserAssistantDetail
from assistant.viewsets import UserAssistantDetail
# from assistants.viewsets import UserAssistantDetail
from inventory.viewsets import BoxViewSet

router = routers.DefaultRouter()
router.register(r'trainers', TrainerViewSet)
router.register(r'ntags', NFCTagViewSet)
router.register(r'ntag-designs', NFCTagDesignViewSet)
router.register(r'assistants', UserAssistantDetail)
router.register(r'boxes', BoxViewSet)
