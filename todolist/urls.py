from django.urls import path
from .views import TodoListView, TodoListDetailView, TaskDeleteView, ProjectDeleteView, next_state


urlpatterns = [
    path('', TodoListView.as_view(), name='projects'),
    path('<int:pk>/', TodoListDetailView.as_view(), name='project'),
    path('delete/task/<int:pk>/', TaskDeleteView.as_view(), name='delete-task'),
    path('delete/proj/<int:pk>/', ProjectDeleteView.as_view(), name='delete-project'),
    path('next/<int:pk>/', next_state, name='next'),

]
