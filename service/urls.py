from django.urls import path

from .views import serviceview

urlpatterns = [
    path('', serviceview, name='service'),
]