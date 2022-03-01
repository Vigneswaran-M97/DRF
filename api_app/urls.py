from django.urls import path
from api_app import views


urlpatterns = [
    path('movie/',views.PhonelistView.as_view()),
    path('movie/<int:pk>',views.PhonelistDetailView.as_view()),
]