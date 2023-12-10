from django.urls import path
from . import views
urlpatterns = [
    path('',views.show , name='show'),
    path('edit_musician/<int:id>',views.edit_musician , name='edit_musician'),
]