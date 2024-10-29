from django.urls import path
from .views import blogView, indexView, detailView

urlpatterns = [
    path('', indexView, name='index'),
    path('blog/', blogView, name='blog'),
    path('blog/<int:pk>/', detailView, name='detail'),
]
