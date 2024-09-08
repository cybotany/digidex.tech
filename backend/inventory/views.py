from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required

from nearfieldcommunication.models import NfcTag

def link(request):
    """
    Handles the initial logic for an NFC tag link.
    Redirects to the entity if it exists, or passes to the protected view.
    """
    # Separation character "x" is automatically mirrored
    # between UID mirror and NFC counter mirror.
    mirrored_values = request.GET.get('m', None)
    if not mirrored_values or 'x' not in mirrored_values:
        messages.error(request, _('Invalid NFC tag URI.'))
        return redirect('/')

    serial_number, scan_counter = mirrored_values.split('x')
    if not serial_number:
        # MIRROR_BYTE or MIRROR_PAGE is not set properly
        messages.error(request, _('NFC Tag improperly configured.'))
        return redirect('/')

    ntag = get_object_or_404(
        NfcTag.objects.select_related('link'),
        serial_number=serial_number
    )
    ntag.log_scan(request.user, scan_counter)

    # Need better handling
    if hasattr(ntag, 'link'):
        return redirect(ntag.link.url)
    return protected_link(request, ntag)

@login_required
def protected_link(request, ntag):
    """
    Handles the logic that requires the user to be logged in.
    Redirects to the NFC tag management page or shows error messages.
    """
    ntag_user = ntag.user
    # Check if the tag is already owned by another user
    if ntag_user and ntag_user != request.user:
        messages.error(request, _('Tag registered by another user.'))
        return redirect('/')

    # If the tag is not owned, assign it to the current user
    if not ntag_user:
        ntag.user = request.user
        ntag.save()
        messages.success(request, _('NFC tag registered successfully.'))

    user_inv_page = request.user.get_inventory_page()
    return redirect(user_inv_page.url)