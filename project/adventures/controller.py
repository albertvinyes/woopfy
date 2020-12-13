from django.db import models
from django.core import serializers
from django.core.serializers import serialize
from accommodations.models import Accommodation
from activities.models import Activity
from transports.models import Transport
from adventures.models import Adventure
from cities_app.models import City

class AdventureController():

    def filter_by_date_and_location():
        # return if it's not closed
        return "1"

    def create_adventure(adv_name, adv_description, adv_location, adv_date_start, adv_date_end):
        try:
            adv = Adventure.objects.create(
                    name=adv_name,
                    description=adv_description,
                    location=adv_location,
                    date_start=adv_date_start,
                    date_end=adv_date_end,
                    closed=False)
            return adv.id
        except:
            return "Error"

    def edit_adventure(id, adv_name, adv_description, adv_location, adv_date_start,adv_date_end):
        try:
            adv = Adventure.filter(pk=id).update(
                    name=adv_name,
                    description=adv_description,
                    location=adv_location,
                    date_start=adv_date_start,
                    date_end=adv_date_end)
            return "Success"
        except:
            return "Error"

    def create_activity(id_adventure, activity_name, activity_description, activity_start, activity_location):
        try:
            adv = Adventure.objects.filter(pk=id_adventure)
            if not adv.exists():
                return "Adventure ID " + str(id_adventure) + " not found"
            adv = Adventure.objects.get(pk=id_adventure)
            Activity.objects.create(
                    name=activity_name,
                    description=activity_description,
                    start=activity_start,
                    location=activity_location,
                    adventure=adv)
            return "Success"
        except:
            return "Error"

    def edit_activity(id_activity, activity_name, activity_description, activity_start, activity_location):
        try:
            Activity.filter(pk=id_activity).update(
                name=activity_name,
                description=activity_description,
                start=activity_start,
                location=activity_location)
            return '1'
        except:
            return "Error"

    def create_accommodation(id_adventure, accomodation_name, accomodation_location, accomodation_date_start, accomodation_date_end):
        try:
            adv = Adventure.objects.filter(pk=id_adventure)
            if not adv.exists():
                return "Adventure ID " + str(id_adventure) + " not found"
            adv = Adventure.objects.get(pk=id_adventure)
            Accommodation.objects.create(
                    name=accomodation_name,
                    location=accomodation_location,
                    date_start=accomodation_date_start,
                    date_end=accomodation_date_end,
                    adventure=adv)
            return "Success"
        except:
            return "Error"

    def edit_accommodation(id_accommodation, accomodation_name, accomodation_location, accomodation_date_start, accomodation_date_end):
        try:
            Accommodation.objects.filter(pk=id_accommodation).update(
                    name=accomodation_name,
                    location=accomodation_location,
                    date_start=accomodation_date_start,
                    date_end=accomodation_date_end,
                    adventure=adv)
            return "Success"
        except:
            return "Error"

    def create_transport(id_adventure, transport_name, transport_info, type, departure, arrival, date_time, location):
        try:
            adv = Adventure.objects.filter(pk=id_adventure)
            if not adv.exists():
                return "Adventure ID " + str(id_adventure) + " not found"
            adv = Adventure.objects.get(pk=id_adventure)
            Transport.objects.create(
                    name=transport_name,
                    information=transport_info,
                    transport_type=type,
                    is_departure=departure,
                    is_arrival=arrival,
                    departure_date=date_time,
                    departure_location=location,
                    adventure=adv)
            return "Success"
        except:
            return "Error"

    def edit_transport(id_adventure, transport_name, transport_info, type, departure, arrival, date_time, location):
        try:
            Transport.objects.filter(pk=id_adventure).update(
                    name=transport_name,
                    information=transport_info,
                    transport_type=type,
                    is_departure=departure,
                    is_arrival=arrival,
                    departure_date=date_time,
                    departure_location=location)
            return "Success"
        except:
            return "Error"

    def is_adventure_closed(id_adventure):
        try:
            adv = Adventure.objects.filter(pk=id_adventure)
            if not adv.exists():
                return "Adventure ID " + str(id_adventure) + " not found"
            adv = Adventure.objects.get(pk=id_adventure)
            return adv.closed
        except:
            return "Error"

    def close_adventure(id_adventure):
        try:
            adv = Adventure.objects.filter(pk=id_adventure)
            if not adv.exists():
                return "Adventure ID " + str(id_adventure) + " not found"
            adv = Adventure.objects.get(pk=id_adventure)
            adv.closed = True
            adv.save()
            return "Sucess"
        except:
            return "Error"

    def open_adventure(id_adventure):
        try:
            adv = Adventure.objects.filter(pk=id_adventure)
            if not adv.exists():
                return "Adventure ID " + str(id_adventure) + " not found"
            adv = Adventure.objects.get(pk=id_adventure)
            adv.closed = False
            adv.save()
            return "Sucess"
        except:
            return "Error"

    def get_all_adventures():
        adventures = Adventure.objects.all()
        adventures = serializers.serialize('json',adventures)
        return adventures

    def get_activities(id_adventure):
        activities = Activity.objects.filter(adventure=id_adventure)
        activities = serializers.serialize('json',activities)
        return activities

    def get_accomodations(id_adventure):
        accommodations = Accommodation.objects.filter(adventure=id_adventure)
        accommodations = serializers.serialize('json',accommodations)
        return accommodations

    def get_transports(id_adventure):
        transports = Transport.objects.filter(adventure=id_adventure)
        transports = serializers.serialize('json',transports)
        return transports

    def get_cities_starting_with(lookup_str, verbose):
        # name__istartswith is case insensitive, it matches when the city name starts with the sring
        query = City.objects.filter(name__istartswith=lookup_str).order_by('-population')
        # fields we want to retrieve from the city
        if (not verbose):
            fields = ('name','display_name', 'population')
            serialized_query = serialize('json', query, fields=fields)
        else:
            serialized_query = serialize('json', query)
        return serialized_query

    def delete_adventure(id):
        adv = Adventure.objects.filter(pk=id)
        if not adv.exists():
            return "Adventure ID "+ str(id) + " not found"
        dlt = adv.delete()
        return dlt

    def delete_activity(id):
        try:
            act = Activity.objects.filter(pk=id)
            if not adv.exists():
                return "Activity ID "+ str(id) + " not found"
            dlt = act.delete()
            return dlt
        except:
            return "Error"

    def delete_accomodation(id):
        try:
            accm = Accommodation.objects.filter(pk=id)
            if not adv.exists():
                return "Accommodation ID "+ str(id) + " not found"
            dlt = accm.delete()
            return dlt
        except:
            return "Error"

    def delete_transport(id):
        try:
            adv = Transport.objects.filter(pk=id)
            if not adv.exists():
                return "Transport ID "+ str(id) + " not found"
            dlt = adv.delete()
            return dlt
        except:
            return "Error"
