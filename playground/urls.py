from django.urls import path

from .views import LongTaskAPIView, ResultAPIView

app_name = 'playground'

urlpatterns = [
    path('start/', LongTaskAPIView.as_view(), name='start'),
    path('result/<str:token>/', ResultAPIView.as_view(), name='result')
]
