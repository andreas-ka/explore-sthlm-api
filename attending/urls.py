from django.urls import path
from attending import views

urlpatterns = [
    path('attend/', views.AttendList.as_view()),
    path('attend/<int:pk>/', views.AttendDetailList.as_view()),
]