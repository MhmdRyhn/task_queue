from celery.result import AsyncResult
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from task_queue import celery_app
from .serializers import LongAddSerializer
from .tasks import long_add


class LongTaskAPIView(APIView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = LongAddSerializer(data=request.data)

        if serializer.is_valid():
            calc_queue = long_add.delay(serializer.validated_data['number'])
            return Response({'task_id': calc_queue.id})
        return Response({'errors': serializer.errors})


class ResultAPIView(APIView):
    def get(self, request, token, *args, **kwargs):
        result = AsyncResult(str(token), app=celery_app)
        if result.state == 'SUCCESS':
            response = Response({
                'status': result.state,
                'task_id': token,
                'result': result.get()
            }, status=status.HTTP_200_OK)
            # deletes the task after retrieving from the queue
            result.revoke(terminate=True)
        else:
            response = Response({
                'status': result.state,
                'task_id': token,
            })
        return response
