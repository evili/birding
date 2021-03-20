from django.urls import path

from . import views

urlpatterns = [
    path('', views.CladesHomeView.as_view(), name='clades-home'),
    path('search/', views.CladesSearchView.as_view(), name='clades-search'),
]
