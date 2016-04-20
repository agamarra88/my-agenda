from rest_framework import serializers

from models import MyGroups


class MyGroupsSerializer(serializers.ModelSerializer):
    created = serializers.CharField(source='created_at')

    class Meta:
        model = MyGroups
        fields = ('id', 'groups', 'user')
