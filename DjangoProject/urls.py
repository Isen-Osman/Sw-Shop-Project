from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

import orders.views
from app import views
from wishlist import views as wishlist_views
from django.urls import path

urlpatterns = [
    # path('accounts/', include('allauth.urls')),  # AllAuth URL-и

    path('admin/', admin.site.urls),

    path('', views.recently_added_products, name='home'),
    path('product/add/', views.product_add, name='product_add'),
    path('product/<int:product_id>/delete/', views.product_delete, name='product_delete'),
    path('product/<int:product_id>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/', views.product_list, name='products'),

    path('wishlist', wishlist_views.wishlist_view, name='wishlist'),
    path('add/<int:product_id>/', wishlist_views.wishlist_add, name='wishlist_add'),
    path('remove/<int:product_id>/', wishlist_views.wishlist_remove, name='wishlist_remove'),

    path('admin/', admin.site.urls),
    path('create-order/', orders.views.create_order, name='create_order'),
    path('order-success/<int:order_id>/', orders.views.order_success, name='order_success'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
