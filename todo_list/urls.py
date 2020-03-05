from django.contrib import admin
from django.urls import path

from .views import task_view, tasks_view

urlpatterns = [
    path("tasks", tasks_view),
    path("tasks/<int:pk>", task_view),
    path('admin/', admin.site.urls),
]
