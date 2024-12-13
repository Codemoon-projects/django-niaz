from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from models.blogsModel.models import Blogsmodel
from models.blogsModel.comments import Comment
from rest_framework import serializers


class BlogsComponentSerializer(serializers.ModelSerializer):
    
    commentsCount = serializers.IntegerField()
    
    class Meta:
        model = Blogsmodel
        exclude = ["desc", 'blogText']

class BlogsView(APIView):
    
    def get(self, request):
        
        
        param = request.GET
        options = {}
        
        
        if 'search' in param.keys():
            options['name__contains'] = param['search']
        
        if 'category' in param.keys():
            options['catgegory_id'] = param['category']
        

        blogs = Blogsmodel.objects.filter(**options)
        res =  BlogsComponentSerializer(blogs, many=True).data
        
        return Response(res, status=status.HTTP_200_OK)
    
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields =  "__all__"

class BlogSerializer(serializers.ModelSerializer):
    
    comments = CommentSerializer(many=True)
    
    class Meta:
        model = Blogsmodel
        fields =  "__all__"

    
class BlogView(APIView):
    
    def get(self, request, pk):
        blog = Blogsmodel.objects.get(
            pk=pk
        )
        
        res = BlogSerializer(blog).data
        
        return Response(res, status=status.HTTP_200_OK)
    
    

        
        