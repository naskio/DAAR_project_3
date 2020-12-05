"""CV_BANK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .settings import DEBUG, MEDIA_ROOT, STATIC_ROOT, STATIC_URL, MEDIA_URL
import debug_toolbar

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),  # adding Login/Logout to the browsable API.
    # django JET
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('i18n/', include('django.conf.urls.i18n')),
    # API
    # path('api/v1/', include('apps.main.urls')),
    # admin
    path('', admin.site.urls),
    # path('admin/', admin.site.urls),
]

# Static & Media
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)

# Debug Toolbar
if DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
