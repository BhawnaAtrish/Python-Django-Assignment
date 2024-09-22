from django.urls import path
from . import views
from .views import home


urlpatterns = [
    path('', home, name='home'),
    path('top-customers/', views.top_customers_view, name='top_customers'),
]
