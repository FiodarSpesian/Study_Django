from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/<int:user_id>/<int:days>', views.products, name='products'),

]