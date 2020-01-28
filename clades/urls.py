from django.urls import path

from .views import CladesHomeView, CladesSearchView

urlpatterns = [
    path('', CladesHomeView.as_view(), name='clades-home'),
    path('search/', CladesSearchView.as_view(), name='clades-search'),
]

