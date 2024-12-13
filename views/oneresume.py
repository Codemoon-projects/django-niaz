from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from models.resomeModel.models import ResomeModel
from models.blogsModel.comments import Comment
from rest_framework import serializers
from user.models import UsersType



class ResomeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ResomeModel
        fields = "__all__"

class OneResumeView(APIView):
    def put(self, request, pk):

        data = request.data
        user = request.user

        resume = ResomeModel.objects.get(
            repotage__fromKarfarma__user_id = user.pk,
            id=pk
        )
        resume.status = data['status']
        if 'datetime' in data:
            resume.datetime = data['datetime']
        resume.save()
        result = ResomeSerializer(resume).data


        return Response(result, status=status.HTTP_200_OK)