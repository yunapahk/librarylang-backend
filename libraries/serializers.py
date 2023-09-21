from .models import Library
from rest_framework import serializers

## Class TodoSerializer is a subclass of serializers.HyperlinkedModelSerializer.
## For serializing and deserializing data into representations such as json.
class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    ## Meta class is for configuring the TodoSerializer class.
    class Meta:
        # model to serialize
        model = Library
        # fields to show in json
        fields = ('id', 'name', 'language')