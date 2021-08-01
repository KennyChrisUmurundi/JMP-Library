from django.shortcuts import get_object_or_404
from .models import Library
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    print("sooooooooooooooooooooooooooooooooomeeeeeeeeeeeeeeee")
    ipn = sender
    print('the senderrrrrrr',sender)
    print('theeeeeeeippppnnnn',ipn)
    print(ipn.invoice)
    if ipn.payment_status == 'Completed':
        # payment was successful
        # library = get_object_or_404(Library, id=ipn.library_id)
        # library.plan = ipn.plan
        print('success')