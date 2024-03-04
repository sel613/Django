from . import views
from django.urls import path
app_name = 'food'
urlpatterns = [
    path('',views.IndexClassView.as_view(), name ='index'),
    path('item/',views.item,name='item'),
    path('item/saveditem/',views.saveditem,name ="saveditem"),
    path('<int:pk>/',views.FoodDetail.as_view(),name ="detail"),
    path('add',views.CreateItem.as_view(),name='add_item'),
    path('edit/<int:id>/',views.edit_item,name="edit_item"),
    path('delete/<int:id>/',views.delete_item,name="delete_item"),
]