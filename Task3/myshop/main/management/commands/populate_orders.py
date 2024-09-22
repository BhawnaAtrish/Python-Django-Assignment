from django.core.management.base import BaseCommand
from main.models import Order 
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Populate Order model with dummy data'

    def handle(self, *args, **kwargs):
        customers = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']  # Example customers

        for i in range(10):  
            customer_name = random.choice(customers)
            order_date = timezone.now() - timezone.timedelta(days=random.randint(1, 180))
            status = random.choice(['Pending', 'Completed', 'Cancelled'])
            total_amount = random.uniform(10.0, 500.0)

            Order.objects.create(
                customer=customer_name,
                order_date=order_date,
                status=status,
                total_amount=total_amount
            )
            self.stdout.write(self.style.SUCCESS(f'Order {i+1} created for {customer_name}'))
