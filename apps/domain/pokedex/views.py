import requests
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from models_controller.models.tbl_pokemon import TblPokemon
from models_controller.models.mid_favorite_pokemon import MidFavoritePokemon
from models_controller.models.tbl_account import TblAccount
from .serializer import PokemonListSerializer, PokemonDetailSerializer


class PokemonListAPIView(views.APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        """
        一覧ページの表示情報を取得する
        """
        pokemons = TblPokemon.objects.filter(generation=1)
        max_generation = get_generation_cnt()
        serialized_pokemons = PokemonListSerializer(pokemons, many=True)
        ret = {
            'pokemons': serialized_pokemons.data,
            'max_generation': max_generation,
        }
        return Response(ret)

class PokemonDetailAPIView(views.APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        """
        詳細ページの表示情報を取得する
        """
        pk = self.kwargs.get('id')
        pokemon = get_object_or_404(TblPokemon, pk=pk)
        serializer = PokemonDetailSerializer(instance=pokemon, context={"request": self.request,})
        return Response(serializer.data, status.HTTP_200_OK)

def get_generation_cnt():
    """
    世代数を取得
    """
    url = f'https://pokeapi.co/api/v2/generation'
    res = requests.get(url, timeout=10)
    info = res.json()
    return info['count']

@csrf_exempt
@api_view(['POST'])
def select_generation(request):
    """
    選択された世代のポケモンを表示する情報を返却する
    """
    if request.data != 0:
        pokemons = TblPokemon.objects.filter(generation=request.data)
    else:
        pokemons = TblPokemon.objects.all()
    serialized_pokemons = PokemonListSerializer(pokemons, many=True)
    ret = {
        'pokemons': serialized_pokemons.data,
    }
    return Response(ret)

class GetAllFavoritePokemonAPIView(views.APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        """
        全てのお気に入りポケモンを取得する
        """
        username = request.user.username
        mid_favorite_pokemon = TblPokemon.objects.filter(midfavoritepokemon__username=username)
        serialized_pokemons = PokemonListSerializer(mid_favorite_pokemon, many=True)
        ret = {
            'pokemons': serialized_pokemons.data,
        }
        return Response(ret, status.HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
def search_pokemon_name(request):
    """
    受け取った文字列を名前に含むポケモンの一覧を取得
    """
    if request.data != '' and request.data != None:
        pokemons = TblPokemon.objects.filter(pokemon_name__icontains=request.data['pokemon_name'])
    else:
        pokemons = TblPokemon.objects.all()
    pokemons = TblPokemon.objects.filter(pokemon_name__icontains=request.data['pokemon_name'])
    serialized_pokemons = PokemonListSerializer(pokemons, many=True)
    ret = {
        'pokemons': serialized_pokemons.data,
    }
    return Response(ret)

class ToggleFavoriteStateAPIView(views.APIView):
    permission_classes = (IsAuthenticated,)
    
    def put(self, request, *args, **kwargs):
        """
        お気に入り状態を更新する
        """
        pokedex_id = request.data['pokedex_id']
        username = request.user.username
        mid_favorite_pokemon = MidFavoritePokemon.objects.filter(username=username, pokedex_id=pokedex_id)
        if mid_favorite_pokemon.exists():
            mid_favorite_pokemon.delete()
        else:
            pokemon = TblPokemon.objects.get(pokedex_id=pokedex_id)
            account = TblAccount.objects.get(username=username)
            new_record = MidFavoritePokemon(pokedex_id=pokemon, username=account)
            new_record.save()
        return Response(status.HTTP_200_OK)



class CheckFavoriteStateAPIView(views.APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        """
        お気に入り状態を確認する
        """
        pokedex_id = request.data['pokedex_id']
        username = request.user.username
        mid_favorite_pokemon = MidFavoritePokemon.objects.filter(username=username, pokedex_id=pokedex_id)
        response = {
            'is_favorite': mid_favorite_pokemon.exists()
        }
        return Response(response, status.HTTP_200_OK)