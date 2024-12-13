from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from models.contactModel.models import Contactmodel


class Contact(APIView):
    
    def post(self, request, ):
        
        data = request.data
        
        
        contact = Contactmodel.objects.create(
        title=data['title'],
        desc=data['desc'],
        )
        
        contact.save()
        
        return Response(status=status.HTTP_200_OK)