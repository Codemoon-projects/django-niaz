from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from user.models import AllUsers


class KifPoolview(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        
        user = request.user
        if user.dataAccepted == False:
            return Response("اطلاعات تکمیل نیست", status=status.HTTP_400_BAD_REQUEST)
        
        user.kifpool += request.data["price"]
        user.save()
        return Response(status=status.HTTP_200_OK)