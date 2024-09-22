from django.http import HttpResponse
from django.shortcuts import render
from .models import Order

def home(request):
    return HttpResponse("Navigate to `/top-customers/` to view the top 5 customers who have spent the most in the last 6 months.")

def top_customers_view(request):
    top_customers = Order.top_customers_last_6_months()
    return render(request, 'top_customers.html', {'top_customers': top_customers})
