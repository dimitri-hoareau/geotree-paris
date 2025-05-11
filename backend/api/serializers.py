from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from trees.models import Tree

class TreeGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Tree
        geo_field = 'location'
        fields = ['id', 'tree_type', 'created_at', 'updated_at', 'created_by']