from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder
from .views import update_vendor_metrics

@receiver(post_save, sender=PurchaseOrder)
def purchase_order_post_save(sender, instance, created, **kwargs):
    update_vendor_metrics(sender, instance, created, **kwargs)
