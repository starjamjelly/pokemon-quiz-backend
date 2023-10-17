from rest_framework import serializers

from models_controller.models.tbl_type import TblType
from models_controller.models.tbl_pokemon import TblPokemon
from models_controller.models.mid_favorite_pokemon import MidFavoritePokemon


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblType
        fields = (
            'type_id',
            'type_name',
            'color_code',
        )

class TypeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblType
        fields = ('color_code',)
        
class PokemonListSerializer(serializers.ModelSerializer):
    types = TypeColorSerializer(many=True)

    class Meta:
        model = TblPokemon
        fields = (
            'pokedex_id',
            'pokemon_name',
            'image_path',
            'types',
        )

class PokemonDetailSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()
    types = TypeSerializer(many=True)

    def get_is_favorite(self, instance):
        useraname = self.context['request'].user.username
        is_favorite = MidFavoritePokemon.objects.filter(pokedex_id=instance.pokedex_id, username=useraname).exists()
        return is_favorite

    class Meta:
        model = TblPokemon
        fields = (
            'pokedex_id',
            'pokemon_name',
            'genus',
            'characteristic',
            'image_path',
            'is_favorite',
            'types',
        )