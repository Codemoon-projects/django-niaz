from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from models.drugstoresModel.models import Drugstoresmodel
from rest_framework import serializers
from models.drugstoresModel.peson import PersonModel
from models.drugstoresModel.city import CityModel


class personseri(serializers.ModelSerializer):
    class Meta:
        model=PersonModel    
        fields = ["id", "name", "phone"]


class citys(serializers.ModelSerializer):
    class Meta:
        model=CityModel
        fields="__all__"

class DrugSerializer(serializers.ModelSerializer):
    person = personseri(read_only=True)
    city = citys(read_only=True)
    class Meta:
        model = Drugstoresmodel
        fields = ["id", "person", "name", "city", "person", "desc", "phone1", "phone2", "image"]
        
        
class DrugView(APIView):
    
    def get(self, request):  
        
        drugStor = Drugstoresmodel.objects.all()
        res = DrugSerializer(drugStor, many=True)
        
        return Response(res.data, status=status.HTTP_200_OK)

class DrugdethView(APIView):

    def get(self, request, pk):
        
        druft = Drugstoresmodel.objects.get(
            pk=pk
        )
        res = DrugSerializer(druft)

        return Response(res.data, status=status.HTTP_200_OK)