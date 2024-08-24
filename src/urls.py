from django.contrib import admin
from django.urls import path, include
from betashop import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('betashop/', include('betashop.urls')),

]
