from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from user.karfarmaModel import Karfarmamodel
from rest_framework import serializers
from models.repotageModel.models import ResomeModel
from models.repotageModel.models import Repotagemodel



class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Karfarmamodel
        field = "__all__"
        
class ProfileView(APIView):
    def get(self, request):
        profile = Karfarmamodel.objects.get(
        user = request.user.userdata
        )
        res = ProfileSerializer(profile, many=True).data
        return Response(res, status=status.HTTP_200_OK)
        



class ResumesSerializer(serializers.ModelSerializer):
    class Meta:
        model=ResomeModel
        fields = "__all__"

class FromKarfarmaSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    class Meta:
        model=Karfarmamodel
        fields = [
            "placeName", 
            'banner', 
            'noFaaliat', 
            'logo', 
            'lat', 
            'long',
            "name",
        ]

class RepotageSerializer(serializers.ModelSerializer):

    resumes = ResumesSerializer(many=True, read_only=True)
    city = serializers.CharField(read_only=True)
    tags = serializers.ListField(read_only=True,
        child=serializers.CharField(read_only=True)
    )
    fromKarfarma = FromKarfarmaSerializer(read_only=True)
    fromKarfarma_id = serializers.IntegerField(write_only=True)

    class Meta:
        model=Repotagemodel
        fields = [
            'id', 
            'title', 
            'price', 
            'saatHamkari', 
            'gender', 
            'nameMotabar', 
            'nezam', 
            'desc', 
            'show', 
            'fori',
            'resumes',
            'city',
            'tags',
            'fromKarfarma',
            'fromKarfarma_id',
        ]
        

class KarfarmaRepotageView(APIView):
    def get(self, request):
        user = request.user.userdata
        repotage = Repotagemodel.objects.filter(
            fromKarfarma=user
        )
        res = RepotageSerializer(repotage, many=True).data
        return Response(res, status=status.HTTP_200_OK)
        
        