from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app import views
from wishlist import views as wishlist_views
from orders import views as order_views

urlpatterns = [
    # AllAuth URL-и
    path('accounts/', include('allauth.urls')),

    # Admin
    path('admin/', admin.site.urls),

    # Home / Products
    path('', views.recently_added_products, name='home'),
    path('products/', views.product_list, name='products'),
    path('product/add/', views.product_add, name='product_add'),
    path('product/<int:product_id>/delete/', views.product_delete, name='product_delete'),
    path('product/<int:product_id>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('search/', views.search_view, name='search'),

    # Collections
    path('collections/', views.collections_page, name='collections'),

    # Wishlist
    path('wishlist/', wishlist_views.wishlist_view, name='wishlist'),
    path('add/<int:product_id>/', wishlist_views.wishlist_add, name='wishlist_add'),

    # Profile & Google login
    path('profile/', views.profile_view, name='profile_page'),
    path('logout/', views.custom_logout, name='logout'),

    # Orders
    path('create-order/', order_views.create_order, name='create_order'),
    path('order-success/<int:order_id>/', order_views.order_success, name='order_success'),
    path('order-confirmation/<int:order_id>/', order_views.order_confirmation, name='order_confirmation'),

    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_view, name='contact'),
    # path('contact/submit/', contact_view, name='contact_submit'),  # ова е важно

    path('category/<str:category_name>/', views.products_by_category, name='category_products'),

    path('products/', views.product_list, name='products'),

    path('wishlist/remove/<int:product_id>/<str:size>/', wishlist_views.wishlist_remove,
         name='wishlist_remove_with_size'),

    path('products/color/', views.products_by_color, name='products_by_color'),

    path('delivery/', order_views.delivery, name='delivery'),
    path('privacy/', views.privacy_cookie, name='privacy_cookie')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
