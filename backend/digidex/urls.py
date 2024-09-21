from django.urls import include, path
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.admin import urls as dashboard_urls
from wagtail import urls as wagtail_urls
from search.views import search
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from ntags.views import link

urlpatterns = [
    path("accounts/", include('allauth.urls')),
    # path("_allauth/", include("allauth.headless.urls")),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("search/", search, name="search"),
    path("link/", link, name="link"),
    path('documents/', include(wagtaildocs_urls)),
    path("dashboard/", include(dashboard_urls)),
    path("", include(wagtail_urls)),
]
