from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required

from .models import NfcTag
from .serializers import NfcTagSerializer

def link(request):
    """
    Handles the initial logic for an NFC tag link.
    Redirects to the entity if it exists, or passes to the protected view.
    """
    mirrored_values = request.GET.get('m', None)
    if not mirrored_values or 'x' not in mirrored_values:
        messages.error(request, _('Invalid NFC tag URI.'))
        return redirect('/')
    
    serial_number, scan_counter = mirrored_values.split('x')
    if not serial_number:
        messages.error(request, _('Invalid NFC tag Serial Number.'))
        return redirect('/')

    ntag = get_object_or_404(
        NfcTag.objects.select_related('user', 'linked_entity'),
        serial_number=serial_number
    )
    ntag.log_scan(request.user, scan_counter)

    if hasattr(ntag, 'linked_entity'):
        return redirect(ntag.linked_entity.url)
    return protected_link(request, ntag)

@login_required
def protected_link(request, ntag):
    """
    Handles the logic that requires the user to be logged in.
    Redirects to the NFC tag management entity or shows error messages.
    """
    ntag_user = ntag.user
    # Check if the tag is already owned by another user
    if ntag_user and ntag_user != request.user:
        messages.error(request, _('Tag registered by another user.'))
        return redirect('/')

    # If the tag is not owned, ask the user if they want to register it
    if not ntag_user:
        if request.method == "POST":
            ntag.user = request.user
            ntag.save()
            messages.success(request, _('NFC tag registered successfully.'))
        else:
            # Show confirmation page
            template = loader.get_template('nearfieldcommunication/register_nfc_tag.html')
            context = {'nfc_tag': ntag}
            return HttpResponse(template.render(context, request))
    user_inv_page = request.user.get_inventory_page()
    return redirect(user_inv_page.url)
