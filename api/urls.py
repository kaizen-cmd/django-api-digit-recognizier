from django.urls import path
from api.views import img_saver

urlpatterns = [
    path("", img_saver)
]