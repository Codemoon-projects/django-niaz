from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from user.karjoModel import Karjomodel
from rest_framework import serializers
from models.repotageModel.models import Repotagemodel



class KarjoSerializer(serializers.ModelSerializer):
    
    user_id = serializers.IntegerField()
    
    class Meta:
        model=Karjomodel
        fields = ["user_id", "type", "fName", "lName", "gender", "referralCode", "knowType"]


class KarjoView(APIView):

    def put(self, request):
        data = request.data
        print(data)
        print(request.user)
        
        if "type" not in data.keys():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        user = request.user
        user.dataAccepted = True #for test
        user.save()

        try:
            karjo = user.userdata
        except Exception as e:
            print("karjo model not found. generate karjo")
            karjo = KarjoSerializer(data={**data, "user_id": user.pk})
            try:
                karjo.is_valid(raise_exception=True)
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            karjo.save()

        return Response(status=status.HTTP_202_ACCEPTED)
    
    
    
    
