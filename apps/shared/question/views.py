import random
from rest_framework import status, views
from rest_framework.response import Response
from django.db.models import Max

from models_controller.models.tbl_pokemon import TblPokemon
from .serializer import QuestionSerializer


class QuestionGetAPIView(views.APIView):
    """
    問題取得用汎用クラス
    """
    def get(question_total_cnt=0):
        # 最大数取得
        get_max = TblPokemon.objects.all().aggregate(Max('pokedex_id'))

        # クエリセット取得
        question_nums = []
        for i in range(int(question_total_cnt)):
            question_num = random.randint(1, get_max['pokedex_id__max'])
            question_nums.append(question_num)

        queryset = TblPokemon.objects.filter(pokedex_id__in = question_nums)
        serializer = QuestionSerializer(instance=queryset,
                                        many=True,
                                        context={'pokedex_id__max': get_max['pokedex_id__max']})

        return Response(serializer.data, status.HTTP_200_OK)