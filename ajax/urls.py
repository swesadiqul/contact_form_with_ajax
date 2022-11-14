from django.urls import path
from .views import *

urlpatterns = [
    path('', ContactView.as_view(), name='contact_form'),
    # path('', contact_form, name='contact_form'),
]
