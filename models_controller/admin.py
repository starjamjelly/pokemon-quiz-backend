from django.contrib import admin

from models_controller.models.tbl_account import TblAccount
from models_controller.models.tbl_type import TblType
from models_controller.models.tbl_pokemon import TblPokemon
from models_controller.models.mid_pokemon_type import MidPokemonType
from models_controller.models.mid_favorite_pokemon import MidFavoritePokemon


admin.site.register(TblAccount)
admin.site.register(TblPokemon)
admin.site.register(TblType)
admin.site.register(MidPokemonType)
admin.site.register(MidFavoritePokemon)
