from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from user.karfarmaModel import Karfarmamodel
from rest_framework import serializers



class KarjoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Karfarmamodel
        exclude = ["user"]


class ChangeData(APIView):
    
    
    def put(self, request):
        data = request.data
        print(data)
        
        if "type" not in data.keys():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        user = request.user
        user.dataAccepted = True
        user.save()
        
        karfarma, isCreated = Karfarmamodel.objects.get_or_create(
            user=user,
            noFaaliat=data['type'],
        )


        try:
            _karfarma = KarjoSerializer(data)
            _karfarma.save()
        except Exception as e:
            print(f"_karfarma{e}")
        
        
        return Response(status=status.HTTP_202_ACCEPTED)
    