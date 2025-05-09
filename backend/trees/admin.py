from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin 
from .models import Tree

@admin.register(Tree)
class TreeAdmin(GISModelAdmin):
    list_display = ('name', 'location')