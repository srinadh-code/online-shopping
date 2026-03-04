# from decimal import Decimal
# from .models import Order

# def apply_first_order_discount(user, total):

#     has_order = Order.objects.filter(user=user).exists()

#     if not has_order:
#         discount = total * Decimal('0.30')
#         final_total = total - discount
#         return final_total, discount, True

#     return total, Decimal('0.00'), False

from decimal import Decimal
from django.utils import timezone
from .models import Order


def apply_first_order_discount(user, total):

    has_order = Order.objects.filter(user=user).exists()

    if not has_order:
        discount = total * Decimal('0.30')
        final_total = total - discount
        return final_total, discount, True

    return total, Decimal('0.00'), False



def mark_order_delivered(order):

    if order.status == "Delivered" and not order.delivered_at:
        order.delivered_at = timezone.now()
        order.save()