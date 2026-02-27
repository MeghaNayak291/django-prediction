from django.urls import path
from . import views

app_name = 'predictor'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('predict/', views.PredictView.as_view(), name='predict'),
    path('result/<int:pk>/', views.ResultView.as_view(), name='result'),
    path('history/', views.HistoryView.as_view(), name='history'),
]
