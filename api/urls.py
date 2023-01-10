from django.urls import path
from .views import CandidatesListView, AdverseActionEmailView, ChargesListView

urlpatterns = [
    path('candidates', CandidatesListView.as_view(), name="candidates_list"),
    path('send_adverse_email', AdverseActionEmailView.as_view(),
         name="send_adverse_email"),
    path('charges', ChargesListView.as_view(),
         name="charges_list_view"),
]
