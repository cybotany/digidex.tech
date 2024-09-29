from django.db import models
from wagtail.models import Orderable, Collection
from wagtail.documents.models import Document, AbstractDocument
from wagtail.images.models import Image, AbstractImage, AbstractRendition


from django.db import models
from wagtail.models import Collection
from wagtail.documents.models import Document, AbstractDocument
from wagtail.images.models import Image, AbstractImage, AbstractRendition


class CollectionMixin(models.Model):
    """
    An abstract model that adds a collection field and manages collection creation and permissions.
    """
    collection = models.OneToOneField(
        Collection,
        on_delete=models.PROTECT,
        related_name='+',
        null=True,
        blank=True
    )

    @staticmethod
    def get_root_collection():
        """
        Gets or creates the root collection for storing user collections.
        """
        root = Collection.get_first_root_node()
        if not root:
            raise Exception("Root collection not found. Please ensure a root collection exists.")
        return root

    @classmethod
    def get_or_create_collection(cls, name, parent):
        """
        Retrieves or creates a collection with the given name under the parent collection.
        """
        try:
            # Try to retrieve an existing collection
            collection = parent.get_children().get(name=name)
        except Collection.DoesNotExist:
            # If not found, create a new child collection
            collection = parent.add_child(instance=Collection(name=name))
        return collection

    class Meta:
        abstract = True


class BaseDocument(Orderable, AbstractDocument):
    """
    A model to store a document with additional fields.

    Attributes:
        caption (str): The caption of the document.

        title (str): The title of the document.
        file (File): The file of the document.
        created_at (datetime): The date and time the document was created.
        file_size (int): The size of the document file.
        file_hash (str): The hash of the document file.
        source (str): The source of the document.
        collection (Collection): The collection the document belongs to.
        uploaded_by_user (User): The user who uploaded the document.
        caption (str): The caption of the document.
        sort_order (int): The order of the document in the collection.
    """

    source = models.CharField(
        blank=True,
        max_length=255
    )
    caption = models.CharField(
        blank=True,
        max_length=250
    )

    admin_form_fields = Document.admin_form_fields + (
        'source', 'caption'
    )


class BaseImage(Orderable, AbstractImage):
    """
    A model to store an image with additional fields.

    Attributes:
        alt (str): The alt text of the image.
        caption (str): The caption of the image.

        title (str): The title of the image.
        file (File): The file of the image.
        width (int): The width of the image.
        height (int): The height of the image.
        created_at (datetime): The date and time the image was created.
        focal_point_x (int): The x-coordinate of the focal point.
        focal_point_y (int): The y-coordinate of the focal point.
        focal_point_width (int): The width of the focal point.
        focal_point_height (int): The height of the focal point.
        file_size (int): The size of the image file.
        file_hash (str): The hash of the image file.
        collection (Collection): The collection the image belongs to.
        uploaded_by_user (User): The user who uploaded the image.
        sort_order (int): The order of the image in the collection.
    """

    alt = models.CharField(
        blank=True,
        null=True,
        max_length=75
    )
    caption = models.CharField(
        blank=True,
        max_length=250
    )

    admin_form_fields = Image.admin_form_fields + (
        'alt', 'caption'
    )


class BaseRendition(AbstractRendition):
    """
    A model to store an image rendition with additional fields.

    Attributes:
        filter_spec (str): The filter specification of the rendition.
        file (File): The file of the rendition.
        width (int): The width of the rendition.
        height (int): The height of the rendition.
        focal_point_key (str): The key of the focal point.
        image (Image): The image the rendition belongs to.
    """

    image = models.ForeignKey(
        BaseImage,
        on_delete=models.CASCADE,
        related_name='renditions'
    )

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )
