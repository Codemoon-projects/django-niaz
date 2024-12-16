from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from user.karjoModel import Karjomodel
from rest_framework import serializers
from models.repotageModel.models import Repotagemodel


class KarjoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karjomodel
        fields = [
            'fName', 'lName', 'birthdate', 'gender', 'lat', 'long',
            'education', 'education_file', 'worked', 'worked_file',
            'nezam', 'nezam_file', 'meliNo', 'meliNo_file',
            'technician', 'technician_file', 'certificate', 'certificate_file',
            'badBack', 'badBack_file', 'retrain', 'retrain_file', 'program',
            'profilePicture'
        ]

    def update(self, instance, validated_data):
        # Handle file uploads
        file_fields = ['education_file', 'worked_file', 'nezam_file', 'meliNo_file',
                       'technician_file', 'certificate_file', 'badBack_file',
                       'retrain_file', 'profilePicture']
        
        for field in file_fields:
            if field in validated_data:
                setattr(instance, field, validated_data[field])

        # Update other fields
        for field, value in validated_data.items():
            if field not in file_fields:
                setattr(instance, field, value)

        instance.save()
        return instance
    
    
class KarjoProfileUpdater(APIView):

    def put(self, request):
        user = request.user
        data = request.data
        try:
            karjo = user.userdata
        except:
            return Response({"error": "Karjo profile not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = KarjoUpdateSerializer(karjo, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
