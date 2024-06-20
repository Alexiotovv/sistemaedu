from django.urls import path
from estadistica.views import *

urlpatterns = [
    path("estadistica/index/", index, name="appestadistica.index")
]
