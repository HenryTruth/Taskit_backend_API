import datetime
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from Todos.api.serializers import TodosInlineUserSerializer

User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    todos = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri',
            'todos'
        ]

    def get_uri(self,obj):
        request = self.context.get('request')
        return api_reverse("api-user:detail", kwargs={'username':obj.username}, request=request)

    def get_todos(self,obj):
        request = self.context.get('request')
        limit = 10
        if request:
            limit_query = request.GET.get('limit')
            try:
                limit = int(limit_query)
            except:
                pass
        qs = obj.todos_set.all()
        data = {
            'uri':self.get_uri(obj) + "todos/",
            'last':TodosInlineUserSerializer(qs.first(),context={'request':request}).data,
            'recent':TodosInlineUserSerializer(qs[:limit], many=True, context={'request':request}).data
        }
        return data

    # def get_todos_list(self, obj):
    #     qs = obj.todos_set.all()
    #     return TodosInlineUserSerializer(qs, many=True).data