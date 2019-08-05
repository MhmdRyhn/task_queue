from celery.result import AsyncResult
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from task_queue import celery_app
from .serializers import LongAddSerializer
from .tasks import long_add


class LongTaskAPIView(APIView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        number_serializer = LongAddSerializer(data=request.data)

        if number_serializer.is_valid():
            calc_queue = long_add.delay(number_serializer.validated_data['number'])
            return Response({'task_queue_token': calc_queue.id})
            # return Response({'number': 'ok'})
        return Response({'verdict': 'Number is too short'})


class ResultAPIView(APIView):
    def get(self, request, token, *args, **kwargs):
        result = AsyncResult(str(token), app=celery_app)
        if result.state == 'SUCCESS':
            return Response({
                'status': result.state,
                'task_queue_token': token,
                'answer': result.get()
            }, status=result.status)
        else:
            return Response({
                'status': 'calculating',
                'task_queue_token': token,
            })
