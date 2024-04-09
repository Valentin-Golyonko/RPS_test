"""
URL configuration for RPS_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# from django.contrib import admin
from django.urls import path

from dj_core.views import (
    SyncDummyView,
    AsyncDummyView,
    async_dummy_foo,
    SyncUserView,
    AsyncUserView,
)

urlpatterns = [
    #    path('admin/', admin.site.urls),
    path("dj_sync_dummy_view", SyncDummyView.as_view(), name="dj_sync_dummy_view"),
    path("dj_async_dummy_view", AsyncDummyView.as_view(), name="dj_async_dummy_view"),
    path("dj_async_dummy_foo", async_dummy_foo, name="dj_async_dummy_foo"),
    #
    path("dj_sync_user_view", SyncUserView.as_view(), name="dj_sync_user_view"),
    path("dj_async_user_view", AsyncUserView.as_view(), name="dj_async_user_view"),
]
