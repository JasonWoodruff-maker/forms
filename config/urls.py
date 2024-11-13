from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("age/", age, name = "age1"),
    path("heyyou/", hey_you, name = "hey"),
    path("order/", food , name = "order")

]
