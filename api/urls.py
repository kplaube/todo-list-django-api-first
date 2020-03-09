from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="TODO List API",
        default_version="v1",
        description="DjangoDay project :D",
        public=True,
    ))

router = DefaultRouter()
router.register(r"tasks", views.TasksViewSet)

urlpatterns = [
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('', include(router.urls)),
]
