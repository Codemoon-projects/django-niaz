from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.models import UsersSerializer
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import AllUsers, UsersSerializer, UsersType
from random import randint
from time import sleep
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hashlib import md5



class LoginTokenOptainer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(LoginTokenOptainer, self).validate(attrs)

        user = UsersSerializer(self.user)

        data.update({'user': user.data})

        return data


class LoginView(TokenObtainPairView):
    serializer_class = LoginTokenOptainer
    
    

def createAuthCode(phone, type):
    print(type)
    user, isCreated = AllUsers.objects.get_or_create(
        username=phone,
        usertype=type,
    )
    password = str(randint(100000, 999999))
    print(f"user {phone} code: {password}")
    
    # hash password for save in database
    hashedPass = md5(password.encode()).hexdigest()+"@niazfarmesi"
    user.set_password(hashedPass)
    user.save()

    while True:
        try:
            # api = Api("09145970504", 'BG!RA')
            # sms_soap = api.sms('soap')
            # res = sms_soap.send_by_base_number(
            #     [password], f"0{phone}", 151469)
            break
        except Exception as e:
            print("sms error in password")
            print(e)
            sleep(5)

    return Response(status=status.HTTP_200_OK)




class SendSMSPhoneView(APIView):
    
    def post(self, request):
        """send user code data"""
        data = request.data
        
        try:
            user = AllUsers.objects.get(
                username=data['phone']
                )
        except Exception as e:
            print(e)

        if user.usertype != data['type']:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        print(data['phone'])
        if "type" not in data.keys():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        # check for user type
        if data['type'] not in [UsersType.KARJO_MODEL, UsersType.KARFARMA_MODEL]:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
        # create auth code
        return createAuthCode(**data)
    

