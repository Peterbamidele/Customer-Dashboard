from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('product/', views.products),
    path('customer/', views.customer),
    # path('status/', views.status),

]
