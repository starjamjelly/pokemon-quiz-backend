import requests
import time
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from models_controller.models.tbl_type import TblType
from models_controller.models.tbl_pokemon import TblPokemon
from models_controller.models.mid_pokemon_type import MidPokemonType
from config.const import COLOR_CODE


@csrf_exempt
def regist_all_pokemons(request):
    """
    ポケモン図鑑データを登録する
    """
    if request.method == 'POST':
        # ポケモンの件数取得
        parent_species_url  = 'https://pokeapi.co/api/v2/pokemon-species'
        parent_species_res  = requests.get(parent_species_url, timeout=5)
        parent_species_info = parent_species_res.json()
        # max_pokemon_id = parent_species_info['count']
        min_pokemon_id = 899
        max_pokemon_id = 1009
        
        for id in range(min_pokemon_id, max_pokemon_id):
            # データ取得
            pokemon_url  = f'https://pokeapi.co/api/v2/pokemon/{id}'
            pokemon_res  = requests.get(pokemon_url, timeout=5)
            pokemon_info = pokemon_res.json()

            species_url  = pokemon_info['species']['url']
            species_res  = requests.get(species_url, timeout=5)
            species_info = species_res.json()

            generation_url  = species_info['generation']['url']
            generation_res  = requests.get(generation_url, timeout=5)
            generation_info = generation_res.json()

            # データ登録
            obj_pokemon = TblPokemon(
                pokedex_id     = pokemon_info['id'],
                pokemon_name   = get_info_jp(species_info['names'], 'name'),
                genus          = get_info_jp(species_info['genera'], 'genus'),
                characteristic = get_info_jp(species_info['flavor_text_entries'], 'flavor_text'),
                generation     = generation_info['id'],
                image_path     = pokemon_info['sprites']['other']['official-artwork']['front_default'],
                created_user   = 'admin',
                updated_user   = 'admin',
            )
            if obj_pokemon.genus == None:
                obj_pokemon.genus = 'ふめい'
            if obj_pokemon.characteristic == None:
                obj_pokemon.characteristic = 'ふめい'
            obj_pokemon.save()
            print(f'{id}:{obj_pokemon.pokemon_name}/ -- success')
            time.sleep(0.5)

        return HttpResponse('--- success add. ---')
    else:
        return HttpResponse('--- no done. ---')

@csrf_exempt
def regist_all_types(request):
    """
    ポケモンのタイプ情報を登録する
    """
    if request.method == 'POST':
        type_kind = 18
        for id in range(1, type_kind + 1):
            # データ取得
            url = f'https://pokeapi.co/api/v2/type/{id}'
            res = requests.get(url, timeout=5)
            type_info = res.json()

            # データ登録
            obj_type = TblType(
                type_id      = type_info['id'],
                type_name    = get_info_jp(type_info['names'], 'name'),
                color_code   = COLOR_CODE[type_info['id']],
                created_user = 'admin',
                updated_user = 'admin',
            )
            obj_type.save()
            print(f'{id}: success')
            time.sleep(0.5)
        return HttpResponse('--- success add. ---')
    else:
        return HttpResponse('--- no done. ---')

@csrf_exempt
def regist_all_pokemon_type_relation(request):
    """
    ポケモンとタイプの紐付け情報を登録する
    """
    if request.method == 'POST':
        # ポケモンの件数取得
        parent_species_url  = 'https://pokeapi.co/api/v2/pokemon-species'
        parent_species_res  = requests.get(parent_species_url, timeout=5)
        parent_species_info = parent_species_res.json()
        # max_pokemon_id = parent_species_info['count']
        min_pokemon_id = 1
        max_pokemon_id = 1009

        for id in range(min_pokemon_id, max_pokemon_id):
            # データ取得
            url = f'https://pokeapi.co/api/v2/pokemon/{id}'
            res = requests.get(url, timeout=10)
            pokemon_info = res.json()

            # データ登録
            for i in range(len(pokemon_info['types'])):
                type_info    = pokemon_info['types'][i]
                type_info_id = get_type_id(type_info)
                obj_pokemon_type = MidPokemonType(
                    pokedex_id   = TblPokemon.objects.get(pokedex_id = pokemon_info['id']),
                    type_id      = TblType.objects.get(type_id = type_info_id),
                    type_slot    = type_info['slot'],
                    created_user = 'admin',
                    updated_user = 'admin',
                )
                obj_pokemon_type.save()
                print(f"{id}(type{type_info['slot']}/{type_info_id}): success")
                time.sleep(0.5)
        return HttpResponse('--- success add. ---')
    else:
        return HttpResponse('--- no done. ---')

def get_info_jp(arr_some_lang_data, key):
    """
    受け取った情報の中で日本語のものを返却する.
    """
    for pick_info in arr_some_lang_data:
        if pick_info['language']['name'] == 'ja-Hrkt':
            return pick_info[key]

def get_type_id(obj_type):
    """
    タイプのコードを取得する.
    """
    find_base = obj_type['type']['url']
    before_str = 'type/'
    before_idx = find_base.find(before_str)
    return find_base[before_idx+5:-1]

def mock_signup(user_name, password, confirm_password):
    print(user_name)
    print(password)
    print(confirm_password)
    return True