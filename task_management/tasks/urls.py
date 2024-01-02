from django.urls import path
from .views import TaskLists, TaskActions

urlpatterns = [
    path('',TaskLists.as_view(),name='gettasks'),
    path('<int:pk>',TaskActions.as_view(),name='actiontasks'),
]