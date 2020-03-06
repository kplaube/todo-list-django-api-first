from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"tasks", views.TasksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
