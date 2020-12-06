from django.urls import path, include, re_path
from rest_framework import permissions, routers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf import settings
from . import views

router = routers.DefaultRouter()
# Main
router.register(r'search', views.SearchViewSet, basename='Search')
router.register(r'resumes', views.ResumeViewSet, basename='Resume')

schema_view = get_schema_view(
    openapi.Info(
        title="CV CATCHER API",
        default_version='v1',
        description="CV CATCHER API, by swagger",
        terms_of_service="https://nask.io/",
        contact=openapi.Contact(email="contact@nask.io"),
        license=openapi.License(name="BSD License"),
    ),
    public=settings.DEBUG,
    permission_classes=(permissions.AllowAny if settings.DEBUG else permissions.IsAuthenticated,),
)

urlpatterns = [
    # documentation
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # DRF
    path('', include(router.urls)),
]
