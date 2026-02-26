from django.urls import path

from .views import predict_api, home, history_view, decor_view

urlpatterns = [
    path('', decor_view, name='landing'),
    path('detect/', home, name='home'),
    path('api/predict/', predict_api),
    path('history/', history_view, name='history'),
]
