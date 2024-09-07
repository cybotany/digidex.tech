from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey


class InventoryPlant(models.Model):
    inventory = ParentalKey(
        'inventory.UserInventory',
        related_name='plants'
    )
    name = models.CharField(
        max_length=255
    )
    description = models.TextField(
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('plant')
        verbose_name_plural = _('plants')
