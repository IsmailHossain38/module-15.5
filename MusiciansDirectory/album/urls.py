from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('delete_mode/<int:id>',views.delete_model,name='delete_model'),
    path('edit_album/<int:id>',views.edit_album,name='edit_album'),
]