from django.urls import path
from .views import blogView, indexView

urlpatterns = [
    path('', indexView, name='index'),
    path('blog/', blogView, name='blog'),
]
