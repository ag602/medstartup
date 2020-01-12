from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('diabriskpred/', views.diabriskpred, name='diabriskpred'),
    path('diabetes_result/', views.diabetes_report, name='diabetes_report'),

]