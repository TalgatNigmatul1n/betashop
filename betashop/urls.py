from django.urls import path

from . import views

app_name = 'betashop'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:id>/', views.indexItem, name='indexItem'),
    

]