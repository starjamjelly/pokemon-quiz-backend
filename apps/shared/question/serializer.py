from rest_framework import serializers
import random

from models_controller.models.tbl_pokemon import TblPokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblPokemon
        fields = (
            'pokedex_id',
            'pokemon_name',
        )

class QuestionSerializer(serializers.Serializer):
    pokedex_id     = serializers.IntegerField()
    pokemon_name   = serializers.CharField()
    genus          = serializers.CharField()
    characteristic = serializers.CharField()
    image_path     = serializers.CharField()
    dummys         = serializers.SerializerMethodField()
    
    def get_dummys(self, obj):
        pokedex_id__max = self.context.get('pokedex_id__max')
        dummy_nums = []
        if obj.pokedex_id == 1:
            dummy_nums.extend([obj.pokedex_id+1, obj.pokedex_id+2])
        elif obj.pokedex_id == pokedex_id__max:
            dummy_nums.extend([obj.pokedex_id-2, obj.pokedex_id-1])
        else:
            dummy_nums.extend([obj.pokedex_id-1, obj.pokedex_id+1])
        dummy_nums.extend([random.randint(1, pokedex_id__max)])
        
        queryset = TblPokemon.objects.filter(pokedex_id__in=dummy_nums)
        serializer = PokemonSerializer(instance=queryset, many=True)
        return serializer.data