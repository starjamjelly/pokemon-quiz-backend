from django.db import models
from config.settings import AUTH_USER_MODEL

class MidFavoritePokemon(models.Model):
    """
    ユーザーごとのお気に入りポケモンを管理するテーブル
    """
    class Meta:
        db_table  = 'mid_favorite_pokemon'
        app_label = 'models_controller'
    
    username     = models.ForeignKey(AUTH_USER_MODEL, to_field='username', on_delete=models.CASCADE, db_column='username')
    pokedex_id   = models.ForeignKey('TblPokemon', on_delete=models.CASCADE, db_column='pokedex_id')
    created_user = models.CharField(max_length=50)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_user = models.CharField(max_length=50)
    updated_at   = models.DateTimeField(auto_now=True)