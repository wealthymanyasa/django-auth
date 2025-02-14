"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from dj_rest_auth.views import PasswordResetConfirmView, PasswordResetView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions



#define schemaview for swagger ui
schema_view = get_schema_view(
    openapi.Info(
        title="API Docs.",
        default_version="v1",
        descripton="APIs on swagger"
    ),
    public=True,
    permission_classes = [permissions.AllowAny]

)

#swagger ui settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("dj_rest_auth.urls")),
    path('auth/registration/', include("dj_rest_auth.registration.urls")),
    path('auth/password/reset/', PasswordResetView.as_view, name="password_reset"),
    path('auth/password/reset/confirm/<str:uidb64>/<str:token>', 
         PasswordResetConfirmView.as_view, name="password_reset_confirm"),
    
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
     path(
        "swagger/", 
        schema_view.with_ui("swagger", cache_timeout=0),
          name="schema-swagger-ui"
    ),
     path(
        "redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]   
