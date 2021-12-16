from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.addshow,name='addshow'),
    path('delete/<int:id>/',views.Delete_Data,name='DeleteData'),
    path('update/<int:id>/',views.update_Data,name='updateData'),
   
]
