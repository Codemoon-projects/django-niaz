from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from models.blogsModel.models import Blogsmodel
from models.blogsModel.category import CategoryModel
from models.blogsModel.writer import WriterModel
from rest_framework import serializers
from views.blogs import BlogsComponentSerializer


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriterModel
        fields = ["id", "name"]
    
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CategoryModel
        fields = "__all__"


class MainView(APIView):
    
    def get(self, request):
        
        blog = Blogsmodel.objects.all()[:3]
        writers = WriterModel.objects.all()
        categories = CategoryModel.objects.all()
        
        res = {
            "blogs": BlogsComponentSerializer(blog, many=True).data,
            "writers": WriterSerializer(writers, many=True).data,
            "categories": CategorySerializer(categories, many=True).data
        }
        
        return Response(res, status=status.HTTP_200_OK)
    
    