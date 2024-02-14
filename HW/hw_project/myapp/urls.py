from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/<int:customer_id>/<int:count_days>', views.customer_products, name='customer_products'),
    path('products/add', views.add_product, name='add_product'),
    path('users/add', views.new_user, name='new_user'),
]