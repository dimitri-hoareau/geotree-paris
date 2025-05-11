from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Tree(models.Model):
    """Model for individual trees (oaks and pines)"""
    TREE_TYPES = [
        ('Quercus', 'Oak'),
        ('Pinus', 'Pine'),
    ]
    tree_type = models.CharField("Tree type", max_length=10, choices=TREE_TYPES)
    location = models.PointField("Location", srid=4326)
    created_at = models.DateTimeField("Created at", auto_now_add=True )
    updated_at = models.DateTimeField("Updated at", auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        related_name="trees_created",
        verbose_name="Added by",
        blank=True
    )
    
    def __str__(self):
        return f"{self.tree_type} - {self.location}"