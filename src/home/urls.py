from django.urls import path
from django.views.generic import TemplateView

from home.views import HomeView, MentionsLegalesView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('mentions_legales', MentionsLegalesView.as_view(), name='mentions_legales'),
]