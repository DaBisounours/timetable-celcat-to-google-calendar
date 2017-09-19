from time import sleep
from urllib.error import URLError

import timetable.downloader as dwn
import timetable.parser as prs


downloaded = False
response = None
attempts = 3

while not downloaded:
    if attempts <= 0:
        print("Aborting process.")
        exit(2)

    try:
        # Download and save webpage (Example)
        # dwn.save_web_page()

        # Download webpage
        response = dwn.get_web_page()

        print("Download successful.")
        downloaded = True

    except URLError:
        print("Could not download the page. Retrying in a sec...")
        attempts -= 1
        sleep(1)

# Create XML Object from raw data
xml_obj = prs.get_xml_timetable_object(response)

# Create Timetable object from XML
timetable = prs.parse_xml_timetable(xml_obj)

# Print timetable
print(timetable.as_csv_data())

# Save CSV File
timetable.save_as_csv_file('timetable.csv')


