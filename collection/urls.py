from django.urls import path
from .views import collectionview

urlpatterns = [
    path('', collectionview, name='collection'),
]
