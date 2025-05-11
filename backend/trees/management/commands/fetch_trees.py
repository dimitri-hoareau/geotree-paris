from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
import requests
from trees.models import Tree

class Command(BaseCommand):
    help = 'Retrieves oak and pine trees from the OpenData Paris API and populates the database with their locations and attributes'

    def handle(self, *args, **options):
        base_url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/les-arbres/records"
        
        def fetch_tree_by_genre(genre):
            print(f"start fetching data for {genre}...")
            limit = 100     
            offset = 0
            data_to_fetch = True
            
            while data_to_fetch:
                url = f"{base_url}?limit={limit}&offset={offset}&refine=genre%3A%22{genre}%22"
                response = requests.get(url)
                data = response.json()
                tree_data = data.get('results', [])
                if not tree_data:
                    print("There is no more data to fetch")
                    data_to_fetch = False
                else:
                    for tree in tree_data:
                        genre = tree.get('genre', 'Unknow')
                        geo_point = tree.get('geo_point_2d', {})
                        lon = round(geo_point.get('lon'), 5)
                        lat = round(geo_point.get('lat'), 5)
                        point = Point(lon, lat, srid=4326)
                        
                        #Check if there is already a tree with same coordinates
                        existing = Tree.objects.filter(location=point).exists()

                        if not existing:
                            Tree.objects.create(
                                tree_type=genre,
                                location=point
                            )

                    offset+=limit
                    
        fetch_tree_by_genre("Pinus")
        fetch_tree_by_genre("Quercus")

