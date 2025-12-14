from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


"""Add app's urls"""
app_name = 'task'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('task/<int:task_id>/', views.task, name='task'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('login/', auth_views.LoginView.as_view(template_name='task/login.html') , name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('update/<int:task_id>/', views.update, name='update'),
    path('toggle/<int:task_id>', views.toggle, name='toggle')
]