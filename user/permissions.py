from rest_framework import permissions
from user.models import UsersType



class isKarfarmamodel(permissions.BasePermission):
    
    def has_permission(self, request, view, ):
        if request.user.is_authenticated:
            return True
    
    def has_object_permission(self, request, view, obj, ):
        if request.user.userType == UsersType.KARFARMAMODEL:
            return True