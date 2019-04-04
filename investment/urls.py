from django.urls import path

from investment import views

urlpatterns = [
    path('loans/', views.LoanList.as_view()),
    path('loan/<int:pk>/', views.LoanDetail.as_view()),
    path('investments/', views.InvestmentList.as_view()),
]
