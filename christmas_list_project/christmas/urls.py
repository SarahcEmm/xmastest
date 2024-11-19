from django.urls import path
from . import views

urlpatterns = [
    path('my-lists/', views.my_lists, name='my_lists'),
    path('create-list/', views.create_list, name='create_list'),
    path('list/<int:list_id>/', views.view_list, name='view_list'),
]