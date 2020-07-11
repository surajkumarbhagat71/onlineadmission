from django.contrib import admin
from django.urls import path,include
from public.views import *
urlpatterns = [
    path('',HomeView.as_view(),name='homepage'),
    path('add/',AddRecordView.as_view(),name='addRecord'),
    path('details/<int:pk>/',PeopleDetailView.as_view(),name='item'),
    path('search/',SearchListView.as_view(),name='search'),
]
