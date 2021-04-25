from django.urls import path

from competences.views import CompetenceList

urlpatterns = [
    path('', CompetenceList.as_view(), name='competences'),
]