from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('del/<int:pk>',views.deleteTask,name="deleteTask"),
    path('complete/<int:pk>',views.completeTask,name="completeTask"),
    path('notcomplete/<int:pk>',views.notCompleteTask,name="notCompleteTask"),
    path('edit/<int:pk>',views.editTask,name="editTask"),
    path('saveedit/<int:pk>',views.saveEditForm,name="saveEditTask"),

    
]
