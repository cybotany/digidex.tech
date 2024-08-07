from django import template
from django.urls import reverse
from django.utils.text import slugify

from wagtail.models import Site

from base.models import FooterBanner, FooterParagraph, FooterCopyright
from base.components import ParagraphComponent, ButtonComponent


register = template.Library()

@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page

@register.inclusion_tag('base/includes/footer/banner.html', takes_context=True)
def footer_banner(context):
    fbanner = FooterBanner.objects.filter(live=True).first()

    return {
        'subtitle': fbanner.subtitle if fbanner else "Are you ready",
        'title': fbanner.title if fbanner else "Your next adventure awaits",
        'cta_url': fbanner.cta_url if fbanner else "#",
        'cta_text': fbanner.cta_text if fbanner else "Learn More",
    }

@register.inclusion_tag("base/includes/footer/paragraph.html", takes_context=True)
def get_footer_paragraph(context):
    paragraph = context.get("footer_paragraph", "")

    if not paragraph:
        instance = FooterParagraph.objects.filter(live=True).first()
        paragraph = instance.paragraph if instance else ""

    footer_paragraph = ParagraphComponent(
        text=paragraph,
        line_break=True,
        style='footer'
    )

    return {
        "footer_paragraph": footer_paragraph,
    }

@register.inclusion_tag("base/includes/footer/copyright.html", takes_context=True)
def get_footer_copyright(context):
    footer_copyright = context.get("footer_copyright", "")

    if not footer_copyright:
        instance = FooterCopyright.objects.filter(live=True).first()
        footer_copyright = instance.copyright if instance else "All rights reserved."

    return {
        "footer_copyright": footer_copyright,
    }

@register.inclusion_tag("base/includes/navigation/buttons.html", takes_context=True)
def get_navigation_buttons(context):
    request = context["request"]
    if request.user.is_authenticated:
        user_slug = slugify(request.user.username)
        buttons = [
            ButtonComponent(
                text=request.user.username,
                url=f"/inv/{user_slug}",
                style='nav-button-outline'
            ),
            ButtonComponent(
                text='Logout',
                url=reverse("account_logout"),
                style='nav-button'
            )
        ]   
    else:
        buttons = [
            ButtonComponent(
                text='Login',
                url=reverse("account_login"),
                style='nav-button-outline'
            ),
            ButtonComponent(
                text='Signup',
                url=reverse("account_signup"),
                style='nav-button'
            )
        ]
    return {
            "buttons": buttons,
        }
