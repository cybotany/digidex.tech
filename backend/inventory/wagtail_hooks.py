from wagtail.admin.panels import TitleFieldPanel, FieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import TrainerInventory, InventoryPlant


class TrainerInventoryViewSet(SnippetViewSet):
    model = TrainerInventory

    panels = [
        TitleFieldPanel("name"),
        FieldPanel("description"),
    ]


class InventoryPlantViewSet(SnippetViewSet):
    model = InventoryPlant

    panels = [
        FieldPanel("inventory"),
        FieldPanel("plant"),
        MultiFieldPanel(
            [
                FieldPanel("label"),
                FieldPanel("nfc_tag"),
            ],
            heading="NFC Tag Details"
        ),
    ]

register_snippet(TrainerInventoryViewSet)
register_snippet(InventoryPlantViewSet)