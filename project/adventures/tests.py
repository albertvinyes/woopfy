from adventures.controller import AdventureController
from django.test import TestCase

class AdventureControllerTests(TestCase):
    # TODO: Add 4 edit tests and filter tests
 
    def setUp(self):
        adv_name = "Great test adventure"
        adv_description = "Enjoy a beer while watching Adventure Time"
        adv_location = "Your House"
        adv_date_start = '2018-10-07'
        adv_date_end = '2018-10-14'
        self.id = AdventureController.create_adventure(
                                        adv_name,
                                        adv_description,
                                        adv_location,
                                        adv_date_start,
                                        adv_date_end)

    def test_adventure_created(self):
        self.assertGreater(self.id, 0)

    def test_is_adventure_open(self):
        is_closed = AdventureController.is_adventure_closed(self.id)
        self.assertIs(is_closed, False)

    def test_close_adventure(self):
        AdventureController.close_adventure(self.id)
        is_closed = AdventureController.is_adventure_closed(self.id)
        self.assertIs(is_closed, True)

    def test_open_adventure(self):
        AdventureController.open_adventure(self.id)
        is_closed = AdventureController.is_adventure_closed(self.id)
        self.assertIs(is_closed, False)

    def test_create_activity(self):
        id_adventure = self.id
        activity_name = "a"
        activity_description = "a"
        activity_start = '2018-10-07 21:48:31'
        activity_location = '2018-10-07 21:48:31'
        result = AdventureController.create_activity(
                                        id_adventure,
                                        activity_name,
                                        activity_description,
                                        activity_start,
                                        activity_location)
        self.assertIs(result, "Success")

    def test_create_activity(self):
        id_adventure = self.id
        accomodation_name = "fancy hotel"
        accomodation_location = "barcelona"
        accomodation_date_start = '2018-10-07'
        accomodation_date_end = '2018-10-14'
        result = AdventureController.create_accommodation(
                                        id_adventure,
                                        accomodation_name,
                                        accomodation_location,
                                        accomodation_date_start,
                                        accomodation_date_end)
        self.assertIs(result, "Success")

    def test_create_activity(self):
        id_adventure = self.id
        transport_name = "slow transport"
        transport_info = "ticket 123623623{38}"
        type = '1'
        departure = True
        arrival = False
        date_time = '2018-10-07 21:48:31'
        location = "Sants Estació"
        result = AdventureController.create_transport(
                                        id_adventure,
                                        transport_name,
                                        transport_info,
                                        type,
                                        departure,
                                        arrival,
                                        date_time,
                                        location)
        self.assertIs(result, "Success")

    def test_delete_adventure(self):
        id_adventure = self.id
        result = AdventureController.delete_adventure(id_adventure)
        result = str(result[0])
        self.assertEquals(str(result[0]), '1')
