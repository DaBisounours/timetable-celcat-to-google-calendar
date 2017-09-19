""" Timetable Class

This class is used to represent a full timetable parsed from the source timetable.
It uses the Event class to store all the events

Todo:
    * Write a set of functions to compare timetables using hashed Events

"""


from classes.Event import Event


class Timetable(object):
    """ Constructor
    Sets the event list to empty list
    """
    def __init__(self):
        self.events = []

    """ Method to add event(s) object(s) to the timetable
    @:arg event_s Event object or list of Event objects containing events to be added
    """
    def add(self, event_s):
        if isinstance(event_s, list):
            self.events += event_s
        elif isinstance(event_s, Event):
            self.events.append(event_s)

    """ Method to render timetable as CSV Data string """
    def as_csv_data(self):
        csv = 'Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description,Location,Private\n'
        for event in self.events:
            csv += event.as_csv_row() + '\n'
        return csv

    """ Method to save the timetable as CSV file 
    @:arg filename Name of the file to be created
    """
    def save_as_csv_file(self, filename):
        data = bytes(self.as_csv_data(), 'utf-8')
        with open('output/'+filename, 'wb') as output:
            output.write(data)
