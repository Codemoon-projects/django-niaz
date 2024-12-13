from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from models.drugstoresModel.models import Drugstoresmodel
from rest_framework import serializers


class DrugSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Drugstoresmodel
        fields = "__all__"
        
        
class DrugView(APIView):
    
    def get(self, request):  
        
        drugStor = Drugstoresmodel.objects.all()
        res = DrugSerializer(drugStor, many=True).data
        
        return Response(res, status=status.HTTP_200_OK)