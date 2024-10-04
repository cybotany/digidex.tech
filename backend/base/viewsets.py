from django.utils.translation import gettext_lazy as _
from wagtail.admin.views.generic.chooser import ChooseView
from wagtail.admin.viewsets.chooser import ChooserViewSet
from django.contrib.contenttypes.models import ContentType


class ContentObjectChooserView(ChooseView):

    def get_object_list(self):
        # import requests
        # from django.conf import settings
        # r = requests.get(f"{settings.WAGTAILADMIN_BASE_URLquit}/api/users/")
        # r.raise_for_status()
        # results = r.json()
        # return results
        content_type_id = self.request.GET.get("content_type")
        if content_type_id:
            content_type = ContentType.objects.get(id=content_type_id)
            model_class = content_type.model_class()
            return model_class.objects.all()
        return ContentType.objects.none()


class ContentObjectChooserViewSet(ChooserViewSet):
    model = None
    url_filter_parameters = ["content_type"]
    preserve_url_parameters = ["multiple", "content_type"]
    choose_view_class = ContentObjectChooserView

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.model is None:
            self.model = self.choose_view_class

    def get_queryset(self):
        if not self.model:
            return self.model.objects.none()
        return self.model.objects.all()


content_object_chooser_viewset = ContentObjectChooserViewSet("object_chooser")