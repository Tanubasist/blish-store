from django.contrib import admin
from django.urls import path, re_path
from store import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.static import serve  # <-- Yeh import zaroori hai

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.store_home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    
    path('cart/', views.view_cart, name='view_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    
    path('checkout/', views.checkout, name='checkout'),
    path('success/', views.order_success, name='order_success'),
    
    # Yeh line add kariye taaki live server par media/images load ho sakein:
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]