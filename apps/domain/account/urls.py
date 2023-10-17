from django.urls import path

from apps.domain.account import views as account_view
from rest_framework_simplejwt import views as simplejwt_view


urlpatterns = [
    path('signup/', account_view.AccountRegistration.as_view()),
    path('jwt/create/', simplejwt_view.TokenObtainPairView.as_view()),
    path('jwt/refresh/', simplejwt_view.TokenRefreshView.as_view()),
    path('login/', account_view.NormalAuthentication.as_view()),
]