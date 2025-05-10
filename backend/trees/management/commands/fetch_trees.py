from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
import requests

class Command(BaseCommand):
    help = 'Retrieves oak and pine trees from the OpenData Paris API and populates the database with their locations and attributes'

    def handle(self, *args, **options):
        base_url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/les-arbres/records"
        
        def fetch_tree_by_genre(genre):

            limit = 100     
            offset = 0
            data_to_fetch = True
            
            while data_to_fetch:
                url = f"{base_url}?limit={limit}&offset={offset}&refine=genre%3A%22{genre}%22"
                response = requests.get(url)
                print(url)
                data = response.json()
                tree_data = data.get('results', [])
                if len(tree_data) == 0:
                    print("empty")
                    data_to_fetch = False
                else:
                    for tree in tree_data:
                        genre = tree.get('genre', 'Unknow')
 
                        geo_point = tree.get('geo_point_2d', {})
                        
                        lon = geo_point.get('lon', 'Inconnue')
                        lat = geo_point.get('lat', 'Inconnue')
                        point = Point(lon, lat, srid=4326)
                        print(point)

                    offset+=limit
                    
        fetch_tree_by_genre("Pinus")
        fetch_tree_by_genre("Quercus")

