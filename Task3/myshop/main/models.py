from django.db import models
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta

class Order(models.Model):
    customer = models.CharField(max_length=255)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} by {self.customer}"

    @classmethod
    def top_customers_last_6_months(cls):
        six_months_ago = timezone.now() - timedelta(days=6*30)
        # Filtering orders from the last 6 months
        recent_orders = cls.objects.filter(order_date__gte=six_months_ago)
        # Annotating customers with total amount spent, and ordering by total amount
        top_customer = (recent_orders
                         .values('customer')
                         .annotate(total_spent=Sum('total_amount'))
                         .order_by('-total_spent')[:5])
        return top_customer
