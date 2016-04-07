from rest_framework import serializers

from apps.contacts.serializers import ContactSerializer
from models import MyContact


class MyContactSerializer(serializers.ModelSerializer):
    created = serializers.CharField(source='created_at')
    contact = ContactSerializer()

    class Meta:
        model = MyContact
        fields = ('id', 'contact', )

    def __unicode__(self):
        return "%s" % self.name