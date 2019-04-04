from django.urls import path

from agent import views

urlpatterns = [
    path('banks/', views.BankList.as_view()),
    path('bank/<int:pk>', views.BankDetail.as_view()),
    path('investors/', views.InvestorList.as_view()),
    path('investor/<int:pk>', views.InvestorDetail.as_view()),
]
