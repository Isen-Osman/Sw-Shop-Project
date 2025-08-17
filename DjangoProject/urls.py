from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from app import views
from wishlist import views as wishlist_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # AllAuth URLs
    path('accounts/', include('allauth.urls')),

    # App URLs
    path('',views.recently_added_products, name='home'),
    path('product/add/', views.product_add, name='product_add'),
    path('product/<int:product_id>/delete/', views.product_delete, name='product_delete'),
    path('product/<int:product_id>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/', views.product_list, name='products'),
    path('profile/', views.profile_view, name='profile'),

    # Wishlist URLs
    path('wishlist/', wishlist_views.wishlist_view, name='wishlist'),
    path('wishlist/add/<int:product_id>/', wishlist_views.wishlist_add, name='wishlist_add'),
    path('wishlist/remove/<int:product_id>/', wishlist_views.wishlist_remove, name='wishlist_remove'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
