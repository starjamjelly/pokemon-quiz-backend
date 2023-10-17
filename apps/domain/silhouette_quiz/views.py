from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.shared.question.views import QuestionGetAPIView


class SilhouetteQuizQuestionGetAPIView(views.APIView):
    """
    シルエットクイズの問題を取得する
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        question_total_cnt = request.data['question_total_cnt']
        res = QuestionGetAPIView.get(question_total_cnt=question_total_cnt)
        return Response(res.data, status.HTTP_200_OK)
    
