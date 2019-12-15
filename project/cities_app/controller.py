from django.core.serializers import serialize
from cities_app.models import City


class CityController():
    # Return matching cities according to a start string
    def get_cities_starting_with(lookup_str, verbose):
        # name__istartswith is case insensitive, it matches when the city name starts with the sring
        query = City.objects.filter(name__istartswith=lookup_str)
        # fields we want to retrieve from the city
        if (not verbose):
            fields = ('name','display_name', 'population').order_by('-population')
            serialized_query = serialize('json', query, fields=fields)
        else:
            serialized_query = serialize('json', query)
        return serialized_query
