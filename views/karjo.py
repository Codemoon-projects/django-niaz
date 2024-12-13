from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from user.karjoModel import Karjomodel
from rest_framework import serializers
from views.profile import RepotageSerializer
from models.repotageModel.models import Repotagemodel



class KarjoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Karjomodel
        exclude = ["user"]


class KarjoView(APIView):

    def put(self, request):
        data = request.data
        print(data)
        
        if "type" not in data.keys():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        user = request.user
        user.dataAccepted = True #for test
        user.save()
        try:
            karjo, isCreated = Karjomodel.objects.get_or_create(
                user=user,
                noFaaliat=data['type'],
                )
        except Exception as e: 
            print(f"karjo{e}")
        try:
            _karjo = KarjoSerializer(data)
            _karjo.save()
        except Exception as e:
            print(f"_karjo{e}")
        return Response(status=status.HTTP_202_ACCEPTED)
    