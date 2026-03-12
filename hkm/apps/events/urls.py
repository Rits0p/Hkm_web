from django.urls import path
from .views import *


urlpatterns = [
    path('', events_home, name='events'),
    path('<slug:slug>/', event_detail, name='event_detail'),
]