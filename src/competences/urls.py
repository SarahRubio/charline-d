from django.urls import path

from competences.views import CompetenceList, CompetenceDetail

urlpatterns = [
    path('', CompetenceList.as_view(), name='competences'),
        path('<slug>', CompetenceDetail.as_view(), name='competence-detail'),
]