from .models import Library
from rest_framework import viewsets, permissions
from .serializers import LibrarySerializer

class LibraryViewSet(viewsets.ModelViewSet):
    ## queryset is a list of all Todo objects
    queryset = Library.objects.all()
    # The serializer_class attribute is used to control which serializer class should be used for serializing and deserializing queryset and model instances.
    serializer_class = LibrarySerializer
    # Set permission_classes to allow unrestricted access to the API.
    permission_classes = [permissions.AllowAny]
