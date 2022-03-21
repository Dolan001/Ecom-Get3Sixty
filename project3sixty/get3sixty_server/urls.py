from django.urls import path, include
from . import views

urlpatterns = [
    path('latest-products/', views.LetestProductList.as_view()),
    path('products/search/', views.search),
    path('product/<slug:category_slug>/<slug:product_slug>/', views.ProductDetails.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetails.as_view()),
]