from django.urls import path
from . import views

# registering the app name
app_name = "tasks"

urlpatterns = [
    path("", views.index, name="list"),
    path("update/<str:pk>/", views.updateTask, name="update"),
    path("delete/<str:pk>/", views.deleteTask, name="delete"),

]
