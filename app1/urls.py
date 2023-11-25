
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('delete',views.delete,name='delete'),
    path('edit',views.edit,name='edit'),
    path('detail/<int:id>',views.detail_page,name='detail'),
    path('create_data',views.create_data,name='create_data'),
]
