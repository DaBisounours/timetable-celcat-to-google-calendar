""" Event Class

This class is used to represent a timetable event parsed from the source timetable.

Todo:
    * Write a function to hash an Event instance, in order to compare events
    * Write a function to format data for Google Calendar API (update / insert)

"""

import datetime

""" Dictionary used to convert numbers into weekdays """
DAYS = {'0': "Monday", '1': "Tuesday", '2': "Wednesday", '3': "Thursday", '4': "Friday"}
""" Integer Constant used to adjust the starting week of the source timetable """
BASE_WEEK = 34
""" Year of the timetable """
YEAR = 2017


class Event(object):

    """ Constructor
    @:arg id Identifier given by the source timetable (WARNING:may not be unique!)
    @:arg prettytimes String representing "<starttime>-<endtime> <category>" given by source timetable
    @:arg resources XML object representing varying data attached to this event
    @:arg rawweeks String representing which week is concerned by this event
    @:arg dayofweek String representation of an integer from 0 to 4 representing weekdays from Monday to Friday
    """
    def __init__(self, id, prettytimes, resources, rawweeks, dayofweek=""):
        self.id = id
        self.day = dayofweek
        self.start = prettytimes[0:5]
        self.end = prettytimes[6:11]
        self.category = prettytimes[12:]
        self.resources = resources
        self.week = BASE_WEEK + Event.decode_rawweeks(rawweeks)

    """ String Representation """
    def __repr__(self):
        # module_line = ""
        # if self.has_module():
        #     module_line = " - module:" + self.resources.module.item.cdata
        # return "\n<Event:" + self.id \
        #        + " - week:" + str(self.week) \
        #        + " - day:" + DAYS[self.day] \
        #        + " - info:" + self.category \
        #        + " - time:" + self.start + "->" + self.end \
        #        + module_line \
        #        + ">"
        return self.as_csv_row()

    """ Gets date from event data, formatted DD/MM/YYYY """
    def get_date(self):
        week_date = datetime.datetime.strptime(DAYS[self.day] + " " + str(self.week) + " " + str(YEAR), '%A %W %Y')
        return str(week_date.date().strftime('%d/%m/%Y'))

    """ Decodes rawweeks data to get the actual relative week number from the source string 
    @:arg rawweeks Source 'rawweeks' string
    """
    @staticmethod
    def decode_rawweeks(rawweeks):
        return ([i for i in range(0, len(rawweeks)) if rawweeks[i] == 'Y']+[-1])[0]

    """ Tells if the instance has a defined module """
    def has_module(self):
        if hasattr(self.resources, "module"):
            if hasattr(self.resources.module, "item"):
                return self.resources.module.item.cdata != ''
        return False

    """ Tells if the instance has a given room """
    def has_room(self):
        if hasattr(self.resources, "room"):
            if hasattr(self.resources.room, "item"):
                return self.resources.room.item.cdata != ''

    """ Renders event as a CSV row formatted string """
    def as_csv_row(self):
        module_text = ""
        location_text = ""
        if self.has_module():
            module_text = self.resources.module.item.cdata[11:] + ' (' + self.resources.module.item.cdata[:8] +')' + ' - '

        if self.has_room():
            location_text = self.resources.room.item.cdata + ' - Université Toulouse 3 Paul Sabatier'

        return module_text + self.category + ',' \
            + self.get_date() + ',' \
            + self.start + ',' \
            + self.get_date() + ',' \
            + self.end + ',' \
            + 'FALSE,' \
            + 'Group : ' + self.resources.group.item.cdata + ',' \
            + location_text + ',' \
            + 'TRUE'

