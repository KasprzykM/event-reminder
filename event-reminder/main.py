import sys
import json
import time
from events import Event
from datetime import date
from dateutil.parser import parse

WAIT_TIME = int(sys.argv[2]) if len(sys.argv) >= 3 else 4
DEADLINE_THRESHOLD = int(sys.argv[3]) if len(sys.argv) >= 4 else 7


def load_file(path):
    with open(path) as data_file:
        if data_file.name.endswith('.json'):
            return parse_json(data_file)
        else:
            print("Unsupported file format")
            quit()


def parse_json(data_file):
    data = json.load(data_file)
    events = []
    for entry in data:
        date_obj = parse(entry['date']).date()
        event = Event().date(date_obj).event_type(entry['event_type']).person_name(entry['person_name']).description(
            entry['description'])
        events.append(event)
    return events


def check_dates(events):
    today = date.today()
    event_found = False
    for event in events:
        remaining_days = event.days_to_deadline(today)
        if remaining_days <= DEADLINE_THRESHOLD and remaining_days >= 0:
            input(event)
            event_found = True

    if not event_found:
        print("No upcoming events")
        time.sleep(WAIT_TIME)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No file path in argument")
        time.sleep(WAIT_TIME)
        quit()
    events_list = load_file(sys.argv[1])
    check_dates(events_list)
    quit()
