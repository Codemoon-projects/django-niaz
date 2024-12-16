from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import serializers
from models.repotageModel.models import Repotagemodel
from user.models import UsersType
from models.resomeModel.models import ResomeModel
from views.jobs.list import RepotageSerializer
from models.repotageModel.tags import TagModel


class RepotageOneView(APIView):
    def get(self, request, pk):
        data = request.data
        repotage = Repotagemodel.objects.get(
            pk = pk
        )

        result = RepotageSerializer(repotage)
        
        return Response(result.data, status=status.HTTP_200_OK)