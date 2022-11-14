from django.contrib import admin
from django.urls import path

from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.DivisionViewSet.as_view(), name='index_view'),
]
