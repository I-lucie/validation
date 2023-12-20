# validation/urls.py
from django.urls import path
from .views import register_view
from .views import form_success_view

urlpatterns = [
    path('', register_view, name='participant_form'),
    path('form_success/', form_success_view, name='form_success'),
   
]



