from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('cafe/', BlackgoCafeListView.as_view(),name='cafe_List'),
    path('entrance/', BlackgoUnivEnteranceListView.as_view(), name='entrance'),
    path('academy', BlackgoAcademyList.as_view(), name='academy'),
]