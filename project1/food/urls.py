from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:item_id>/',views.detail,name='detail'),
    path('item/',views.item,name='item'),
    # add items
    path('add',views.create_item,name='create_item'),
    # edit items
    path("update/<int:id>/",views.update_item,name='update_item'),
    # delte item
    path("delete/<int:id>/",views.delete_item,name='delete_item'),

]
