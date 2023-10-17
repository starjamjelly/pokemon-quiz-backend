from django.db import models

class TblPokemon(models.Model):
    """
    ポケモンの基本情報を格納するテーブル
    """
    class Meta:
        db_table = 'tbl_pokemon'
        app_label = 'models_controller'
        ordering = ['pokedex_id']

    pokedex_id     = models.SmallIntegerField(primary_key=True)
    pokemon_name   = models.CharField(max_length=10)
    genus          = models.CharField(max_length=15,  default='未分類', null=True)
    characteristic = models.CharField(max_length=100, default='未登録', null=True)
    generation     = models.SmallIntegerField()
    image_path     = models.CharField(max_length=300)
    created_user   = models.CharField(max_length=50)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_user   = models.CharField(max_length=50)
    updated_at     = models.DateTimeField(auto_now=True)
    types          = models.ManyToManyField('TblType', through='MidPokemonType')