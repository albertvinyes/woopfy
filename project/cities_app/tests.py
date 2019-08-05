from cities_app.controller import CityController
from django.test import TestCase

class CityControllerTests(TestCase):

    def test_search_for_city1(self):
        lookup_name = 'Barcelona'
        verbose = False
        result = CityController.get_cities_starting_with(lookup_name, verbose)
        if lookup_name in result:
            result = True
        else:
            result = False
        self.assertIs(result, True)
