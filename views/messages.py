from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.permissions import IsAuthenticated
from models.messagesModel.models import Messagesmodel

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messagesmodel
        fields = ['id', 'title', 'description', 'type', 'date', 'badges', 'user_can_delete', 'background']


class MessageListView(APIView):

    def get(self, request):
        user = request.user
        queryset = Messagesmodel.objects.filter(
            user_id=user.pk
        )
        
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)
