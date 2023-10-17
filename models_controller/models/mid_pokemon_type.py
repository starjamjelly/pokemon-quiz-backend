from django.db import models

class MidPokemonType(models.Model):
    """
    ポケモンとタイプの紐付けを管理するテーブル
    """
    class Meta:
        db_table = 'mid_pokemon_type'
        app_label = 'models_controller'
    
    pokedex_id   = models.ForeignKey('TblPokemon', on_delete=models.CASCADE, db_column='pokedex_id')
    type_id      = models.ForeignKey('TblType',    on_delete=models.CASCADE, db_column='type_id')
    type_slot    = models.SmallIntegerField()
    created_user = models.CharField(max_length=50)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_user = models.CharField(max_length=50)
    updated_at   = models.DateTimeField(auto_now=True)