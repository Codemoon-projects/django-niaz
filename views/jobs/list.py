from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import serializers
from models.repotageModel.models import Repotagemodel
from user.models import UsersType
from models.resomeModel.models import ResomeModel
from views.profile.profile import RepotageSerializer
from models.repotageModel.tags import TagModel
from views.profile.profile import FromKarfarmaSerializer
from datetime import datetime



class RepotageShowAllSerializer(serializers.ModelSerializer):
    
    tags = serializers.ListField(read_only=True,
        child=serializers.CharField(read_only=True)
    )
    fromKarfarma_logo = FromKarfarmaSerializer(read_only=True)


    class Meta:
        model=Repotagemodel
        fields = "__all__"



class RepotageView(APIView):
    
    
    def get(self, request):

        repotages = Repotagemodel.objects.filter(
            show=True
        )
        result = RepotageShowAllSerializer(repotages, many=True)
        
        return Response(result.data, status=status.HTTP_200_OK)


    def post(self, request):
        try:
            user = request.user.userdata
            data = request.data
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        
        if request.user.usertype == UsersType.KARFARMA_MODEL:
            
            # serializing and validate repotage model
            repotage = RepotageSerializer(data={
                **data,
                "fromKarfarma_id":user.pk,
            })

                
            
            try:
                    
                # add to database
                repotage.is_valid(raise_exception=True)
                repotage_model = repotage.save()
                for tag in data['tags']:
                    TagModel.objects.create(
                        name=tag,
                        repotage=repotage_model
                    )
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_400_BAD_REQUEST)

            # return data
            return Response(repotage.data, status=status.HTTP_200_OK)


            current_datetime = datetime.now()
            date = str(current_datetime).split(" ")
            tarikh = date[0]
            time = date[1].split(":")
            saat = f"{time[0]}:{time[1]}"
            print(tarikh,saat)
            sendMaskSMS(request.user, 288137, [request.user, repotage.data["id"],tarikh, saat ])


        elif user.usertype == UsersType.KARJO_MODEL:
            return Response(status=status.HTTP_200_OK)
            