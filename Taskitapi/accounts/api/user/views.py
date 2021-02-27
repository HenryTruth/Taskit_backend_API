from django.contrib.auth import get_user_model
from rest_framework import permissions, generics
from rest_framework.views import APIView
from .serializers import UserDetailSerializer
from accounts.api.permissions import AnonPermissionOnly
from Todos.models import Todos
from Todos.api.views import TodosAPIView
from Todos.api.serializers import TodosInlineUserSerializer

User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

    def get_serializer_context(self):
        return {'request':self.request}


class UserStatusAPIView(TodosAPIView):
    serializer_class = TodosInlineUserSerializer

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get('username',None)
        if username is None:
            return Todos.objects.none()
        return Todos.objects.filter(user__username=username)

    def post(self, request, *args, **kwargs):
        return Response({"detail":"NOt allowed here"}, status=400)

# class UserStatusAPIView(generics.ListAPIView):
#     serializer_class = TodosInlineUserSerializer
#     search_fields = ('user__username','title')

#     def get_queryset(self, *args, **kwargs):
#         username = self.kwargs.get('username',None)
#         if username is None:
#             return Todos.objects.none()
#         return Todos.objects.filter(user__username=username)