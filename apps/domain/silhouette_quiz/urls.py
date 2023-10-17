from django.urls import path

from . import views


urlpatterns = [
     path('get-question/',
         views.SilhouetteQuizQuestionGetAPIView.as_view(),
         name='get_question'),
]