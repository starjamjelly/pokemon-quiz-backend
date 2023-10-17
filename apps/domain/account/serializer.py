from rest_framework import serializers

from models_controller.models.tbl_account import TblAccount

class AccountRegistrationSerializer(serializers.ModelSerializer):
    """
    サインアップ時のユーザー登録用シリアライザクラス
    """
    class Meta:
        model = TblAccount
        fields = ['username', 'password']
    
    def create(self, validated_data):
        account = TblAccount.objects.create_user(**validated_data)
        return account