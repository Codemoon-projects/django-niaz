from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from models.resomeModel.models import ResomeModel
from models.blogsModel.comments import Comment
from rest_framework import serializers
from user.models import UsersType
from rest_framework import serializers

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResomeModel
        fields = ['id', 'show', 'status', 'desc', 'repotage', 'user', 'datetime']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['datetime'] = instance.datetime.isoformat() if instance.datetime else None
        return representation



    
class ResumeView(APIView):
    
    def get(self, request):
        user = request.user
        data = request.data
        
        if user.usertype == UsersType.KARJO_MODEL:
            resume = ResomeModel.objects.filter(
                user_id = user.pk,
            )
            result = ResumeSerializer(resume, many=True)
            return Response(result.data, status=status.HTTP_200_OK)

        elif user.usertype == UsersType.KARFARMA_MODEL:
            return Response(status=status.HTTP_200_OK)
    

    
    def post(self, request):
        
        try:
            user = request.user.userdata
            data = request.data
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        if request.user.usertype == UsersType.KARJO_MODEL:

            try:
                # add to database
                ResomeModel.objects.get_or_create(
                    repotage_id = data['repotage_id'],
                    desc = data['desc'],
                    user = user
                )
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_400_BAD_REQUEST)

            # return data
            return Response(status=status.HTTP_200_OK)

        elif user.usertype == UsersType.KARFARMA_MODEL:
            return Response(status=status.HTTP_200_OK)