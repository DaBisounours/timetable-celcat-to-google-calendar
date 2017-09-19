""" Parser Module

This module is used to parse downloaded content by converting raw data into explorable XML object.

"""

import untangle
from classes.Timetable import Timetable
from classes.Event import Event, DAYS

""" Creates XML object from raw data 
@:param resource File or Bytes to be decoded 
"""
def get_xml_timetable_object(resource):
    print('Getting object from webpage.')
    return untangle.parse(resource)


""" Parses all the events contained in the XML object 
@:param xml_object root XML object
"""
def parse_xml_timetable(xml_object):
    print('Parsing XML object.')

    xml_events = xml_object.timetable.event
    events = []

    for event in xml_events:
        events.append(
            Event(event["id"],
                  event.prettytimes.cdata,
                  event.resources,
                  event.rawweeks.cdata,
                  event.day.cdata))

    print('Creating Timetable object.')
    timetable = Timetable()
    timetable.add(events)

    return timetable
