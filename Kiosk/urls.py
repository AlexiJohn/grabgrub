from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_menu, name=('main_menu')),
    path('viewcustomers', views.viewcustomers, name=('viewcustomers')),
    path('viewcustomerorders/<int:pk>/', views.viewcustomerorders, name=('viewcustomerorders')),
    path('add_customer',views.add_customer,name=('add_customer')),
    path('edit_customer/<int:pk>/', views.edit_customer, name=('edit_customer')),
    path('viewfood',views.viewfood,name=('viewfood')),
    path('add_food',views.add_food,name=('add_food')),
    path('edit_food/<int:pk>/',views.edit_food,name=('edit_food')),
    path('vieworders',views.vieworders,name=('vieworders')),
    path('delete_order/<int:pk>/',views.delete_order,name=('delete_order')),
    path('add_order', views.add_order, name=('add_order')),
    path('edit_order/<int:pk>/', views.edit_order, name=('edit_order'))
]