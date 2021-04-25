from django.urls import path
from django.views.generic import TemplateView

from contact.views import ContactView

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
]