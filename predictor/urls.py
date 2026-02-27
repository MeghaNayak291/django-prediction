from django.urls import path
<<<<<<< HEAD
from . import views

app_name = 'predictor'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('predict/', views.PredictView.as_view(), name='predict'),
    path('result/<int:pk>/', views.ResultView.as_view(), name='result'),
    path('history/', views.HistoryView.as_view(), name='history'),
=======

from .views import predict_api, home, history_view, decor_view

urlpatterns = [
    path('', decor_view, name='landing'),
    path('detect/', home, name='home'),
    path('api/predict/', predict_api),
    path('history/', history_view, name='history'),
>>>>>>> 009df0ffc57ddd5736de8738092067bf21f48c79
]
