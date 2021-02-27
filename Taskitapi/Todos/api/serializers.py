from rest_framework import serializers
from accounts.api.serializers import UserPublicSerializer
from Todos.models import Todos
from rest_framework.reverse import reverse as api_reverse

class TodosSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    # user = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    class Meta:
        model = Todos
        fields = [
            'uri',
            'id',
            'user',
            'title',
            'completed'
        ]
        read_only_fields = ['user']

    # def get_user(self,obj):
    #     request = self.context.get('request')
    #     user = obj.user
    #     return  UserPublicSerializer(user,read_only=True, context={"request":request}).data

    def get_uri(self,obj):
        request = self.context.get('request')
        return api_reverse('api-todos:detail',kwargs={"id":obj.id}, request=request)

    def validate_title(self, value):
        if len(value)  > 100:
            raise serializers.ValidationError("This is way to short")
        return value


class TodosInlineUserSerializer(TodosSerializer):
    # uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Todos
        fields = [
            'uri',
            'id',
            'title',
            'completed'
        ]

    # def get_uri(self,obj):
    #     return "api/todos/{id}/".format(id=obj.id)

     