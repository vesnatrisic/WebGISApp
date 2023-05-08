from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.MyObtainTokenPairView.as_view(), name="login"),
    path('registration/', views.RegisterView.as_view(), name="registration"),
    path('password_change/', views.ChangePasswordView.as_view(), name="password_change"),
    path('user_status/', views.UserStatusView.as_view(), name="user-status"),
]
