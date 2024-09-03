from django import template
from django.urls import reverse
from django.utils.text import slugify
from wagtail.models import Site

from base.models import FooterSection

register = template.Library()

@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page

@register.inclusion_tag("base/includes/footer.html", takes_context=True)
def get_footer_section(context):
    footer_section = context.get("footer_section", "")

    if not footer_section:
        instance = FooterSection.objects.filter(live=True).first()
        footer_body = instance.body if instance else ""
        footer_copyright = instance.copyright if instance else "All rights reserved."

    return {
        "footer_body": footer_body,
        "footer_copyright": footer_copyright
    }

@register.inclusion_tag("base/includes/navigation.html", takes_context=True)
def get_navigation_buttons(context):
    request = context["request"]
    if request.user.is_authenticated:
        user_slug = slugify(request.user.username)
        buttons = {
            "primary": {
                "text": request.user.username,
                "url": f"/{user_slug}/"
            },
            "secondary": {
                "text": "Logout",
                "url": reverse("account_logout")
            }
        }
    else:
        buttons = {
            "primary": {
                "text": "Login",
                "url": reverse("account_login")
            },
            "secondary": {
                "text": "Signup",
                "url": reverse("account_signup")
            }
        }
    return buttons