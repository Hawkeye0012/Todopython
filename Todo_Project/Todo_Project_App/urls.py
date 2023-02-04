from Todo_Project_App import views
from django.urls import path

urlpatterns = [
    path('', views.TodoTask, name='task'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('cbvhome/', views.TaskListView.as_view(), name='cbvhome'),
    path('cbvdetails/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetails'),
    # Generic detail view TaskDetailView must be called with either an object pk or a slug in the URLconf.
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete'),
]
