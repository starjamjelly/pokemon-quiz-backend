from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password

from models_controller.models.tbl_account import TblAccount
from apps.domain.account.serializer import AccountRegistrationSerializer


class AccountRegistration(generics.CreateAPIView):
    """
    サインアップ時のユーザー登録用APIクラス
    """
    permission_classes = (AllowAny,)
    serializer_class = AccountRegistrationSerializer

class NormalAuthentication(views.APIView):
    """
    ログイン認証用APIクラス
    """
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']
        try:
            account_obj = TblAccount.objects.get(username=username)
        except:
            account_obj = None

        if not account_obj:
            return Response(False)
        if not account_obj.check_password(raw_password=password):
            return Response(False)
        return Response(True)