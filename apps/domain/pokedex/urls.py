from django.urls import path

from . import views


urlpatterns = [
    path('',
        views.PokemonListAPIView.as_view(),
        name='get_list'),
    path('select-generation/',
        views.select_generation,
        name='select_generation'),
    path('search-pokemon-name/',
        views.search_pokemon_name,
        name='search_pokemon_name'),
    path('get-all-favorite-pokemon/',
        views.GetAllFavoritePokemonAPIView.as_view(),
        name='get_all_favorite_pokemon'),
    path('toggle-favorite-state/',
        views.ToggleFavoriteStateAPIView.as_view(),
        name='toggle_favorite_state'),
    path('check-favorite-state/',
        views.CheckFavoriteStateAPIView.as_view(),
        name='check_favorite_state'),
    path('detail/<int:id>/',
        views.PokemonDetailAPIView.as_view(),
        name='get_detail'),
]