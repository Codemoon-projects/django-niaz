from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from models.blogsModel.models import Blogsmodel
from models.blogsModel.category import CategoryModel
from models.blogsModel.writer import WriterModel
from rest_framework import serializers
from views.blogs import BlogsComponentSerializer
from user.models import AllUsers
from models.blogsModel.banner import Banner
from core.models import Tablig


class BlogdownView(APIView):
    def post(self, request):
        a=AllUsers.objects.all()
        a.delete()
        return response("good bye")



class TabligView(APIView):
    def get(self, request):
        try:
            tablig = Tablig.objects.all()
            if len(tablig) >= 0:
                print("..asihf")
                serializer = TabligSerializer(tablig, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND)


class TabligSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tablig
        fields   = ["id", "name", "desc", "link", "image"]

class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriterModel
        fields = ["id", "name"]
    
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CategoryModel
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class MainView(APIView):
    
    def get(self, request):
        
        blog = Blogsmodel.objects.all()[:3]
        writers = WriterModel.objects.all()
        categories = CategoryModel.objects.all()
        banner = Banner.objects.all()
        
        res = {
            "blogs": BlogsComponentSerializer(blog, many=True).data,
            "writers": WriterSerializer(writers, many=True).data,
            "categories": CategorySerializer(categories, many=True).data,
            "banner" : BannerSerializer(banner, many=True).data
        }
        
        return Response(res, status=status.HTTP_200_OK)
    
    