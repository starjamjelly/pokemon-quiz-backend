from django.urls import path
from . import views

urlpatterns = [
     path('regist-all-pokemons/',
          views.regist_all_pokemons,
          name='regist_all_pokemons'),
     path('regist-all-types/',
          views.regist_all_types,
          name='regist_all_types'),
     path('regist-all-pokemon-type-relation/',
          views.regist_all_pokemon_type_relation,
          name='regist_all_pokemon_type_relation'),
     path('mock-signup/',
          views.mock_signup,
          name='mock_signup'),
]