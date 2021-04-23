from django.urls import path
from . import views


urlpatterns = [
    path('', views.index ,name='index'),
    path('add/', views.Add.as_view(), name='add_item'),
    path('delete/<item_id>/', views.delete_item, name= 'delete_item')
]