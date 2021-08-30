from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/dashboard/', views.dashboard_with_pivot, name='admin_dashboard'),
    path('admin/data', views.pivot_data, name='pivot_data'),
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('carts/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),

    path('orders/', include('orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
