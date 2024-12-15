from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from user.karfarmaModel import Karfarmamodel
from django.contrib.auth.models import User
from rest_framework import serializers

class KarfarmamodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karfarmamodel
        fields = ['fName', 'lName', 'email', 'address', 'placeName', 'date', 'website', 'rubika', 'phoneMajazi', 'lat', 'long']

    def validate_email(self, value):
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid email address")
        return value
    
    
class KarfarmaProfileUpdateView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def put(self, request, *args, **kwargs):
        user = request.user
        profile = user.userdata
        
        serializer = KarfarmamodelSerializer(profile, data=request.data, partial=True)
        
        if serializer.is_valid(raise_exception=True):
            # Handle file uploads
            banner = request.FILES.get('banner')
            logo = request.FILES.get('logo')
            
            if banner:
                banner_name = default_storage.save(f'static/banner_file/{user.id}_banner.jpg', ContentFile(banner.read()))
                profile.banner = banner_name
            
            if logo:
                logo_name = default_storage.save(f'static/logo_file/{user.id}_logo.jpg', ContentFile(logo.read()))
                profile.logo = logo_name

            # Save other fields
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)