from django.shortcuts import get_object_or_404
from .models import Library
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from paypal.standard.models import PayPalStandardBase


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    print("sooooooooooooooooooooooooooooooooomeeeeeeeeeeeeeeee")
    ipn_obj = sender
    lib = PayPalStandardBase.objects.get(id=ipn_obj)
    print("the liiib",lib)