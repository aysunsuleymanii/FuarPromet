"""
URL configuration for fuar_promet_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from fuar_promet.views import *

urlpatterns = [
                  # Language switcher
                  path('i18n/', include('django.conf.urls.i18n')),

                  # Core pages
                  path('', home, name='home'),
                  path('about/', about, name='about'),
                  path('contact/', contact, name='contact'),
                  path('our_work/', our_work, name='our_work'),

                  # Admin
                  path('admin/', admin.site.urls),

                  # Products
                  path('products/', products_list, name='products'),
                  path('category/<int:category_id>/', category_products, name='category_products'),
                  path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

                  # Services
                  path('services/', services, name='services'),
                  path('services/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),

                  # Other
                  path('kitchen/', kitchen_view, name='kitchen'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
