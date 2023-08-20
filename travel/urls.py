from . import views
from django.urls import path

urlpatterns = [
    path('region/', views.RegionListAPIView.as_view()),
    path('hotel/', views.HotelListAPIView.as_view()),
    path('order/', views.OrderCreateAPIView.as_view()),

]