from django.urls import path
from .views import CustomLoginView, LogoutView, principal_view




urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('principal/', principal_view, name='principal'),
]