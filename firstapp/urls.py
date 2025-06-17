from django.contrib import admin
from django.urls import path

from firstapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('show/', index)

]