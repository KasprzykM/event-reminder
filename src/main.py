import sys
import json
import time
from pprint import pprint
from events import Event
from datetime import date
from dateutil.parser import parse

DEFAULT_WAIT_TIME = int(sys.argv[2]) if len(sys.argv) >= 3 else 4
DEFAULT_DEADLINE_THRESHOLD = int(sys.argv[3]) if len(sys.argv) >= 4 else 7

def load_file(path):
    with open(path) as data_file:
        if data_file.name.endswith('.json'):
            return parse_json(data_file)
        else:
            print("Unsupported file format")
            quit()

def parse_json(data_file):
    data = json.load(data_file)
    events_list = []
    for entry in data:
        date_obj = parse(entry['date']).date()
        event = Event().date(date_obj).event_type(entry['event_type']).person_name(entry['person_name']).description(entry['description'])
        events_list.append(event)    
    return events_list

def check_dates(events_list):
    today = date.today()
    event_found = False
    for event in events_list:
        remaining_days = event.days_to_deadline(today)
        if remaining_days <= DEFAULT_DEADLINE_THRESHOLD and remaining_days >= 0:
            input(event)
            event_found = True
    
    if not event_found:
        print("No upcoming events")
        time.sleep(DEFAULT_WAIT_TIME)
               
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No file path in argument")
        time.sleep(DEFAULT_WAIT_TIME)
        quit()
    events_list = load_file(sys.argv[1])
    check_dates(events_list)
    quit()