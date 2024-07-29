from django.urls import path
from .views import todo_list, todo_detail

urlpatterns = [
    path('list/', todo_list, name='list'),
    path('detail/<int:pk>/', todo_detail, name='detail'),
]
