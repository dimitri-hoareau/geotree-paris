from rest_framework import viewsets
from trees.models import Tree
from .serializers import TreeGeoSerializer


class TreeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint who display trees.
    """
    queryset = Tree.objects.all()
    serializer_class = TreeGeoSerializer

