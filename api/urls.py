from django.urls import path
from api import views

urlpatterns = [
    path('data/list', views.VcfDataList.as_view(), name='data-list'),
    path('data/row', views.VcfDataRow.as_view(), name='data-row'),
]