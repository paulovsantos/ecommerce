from django.contrib import admin
from django.urls import path
from ecommerce import views
from ecommerce.views import home


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
]