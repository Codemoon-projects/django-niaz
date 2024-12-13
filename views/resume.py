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


    
class ResumeView(APIView):
    
    def get(self, request):

        if request.user.usertype == UsersType.KARJO_MODEL:

            data = request.data
            user = request.user

            resume = ResomeModel.objects.filter(
                user_id = user.pk,
            )
            result = ResomeSerializer(resume, many=True)
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
                resume = ResomeModel.objects.get_or_create(
                    repotage_id = data['repotage_id'],
                    desc = data['desc'],
                    user = user
                )
                _resume = resume.save()
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_400_BAD_REQUEST)

            # return data
            return Response(status=status.HTTP_200_OK)

        elif user.usertype == UsersType.KARFARMA_MODEL:
            return Response(status=status.HTTP_200_OK)