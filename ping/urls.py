from django.urls import re_path
from ping.views import status

urlpatterns = [
    re_path(r'^$', status, name='status'),
]

