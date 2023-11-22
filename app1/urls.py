
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('detail/<int:id>',views.detail_page,name='detail'),
]
