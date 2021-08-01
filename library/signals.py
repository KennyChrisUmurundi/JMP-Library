from django.shortcuts import get_object_or_404
from .models import Library
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
# from paypal.standard.models import PayPalStandardBase
from paypal.standard.ipn.signals import payment_was_successful


def process_subscription(sender, **kwargs):
    ipn_obj = sender
    # Undertake some action depending upon `ipn_obj`.
    print(ipn_obj)

payment_was_successful.connect(process_subscription)