import sys
import json
import time
import argparse
from events import Event
from datetime import date
from dateutil.parser import parse


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

def check_dates(events, wait_time, deadline_threshold):
    today = date.today()
    event_found = False
    for event in events:
        remaining_days = event.days_to_deadline(today)
        if remaining_days <= deadline_threshold and remaining_days >= 0:
            input(event)
            event_found = True

    if not event_found:
        print("No upcoming events")
        time.sleep(wait_time)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--filepath", help="specify path to data file", required=True)
    parser.add_argument("--wait_time", help="time to wait before window disappears", type=int, default=4)
    parser.add_argument("--deadline", help="how many days before event to set reminder for", type=int, default=7)
    args = parser.parse_args()
    events_list = load_file(path=args.filepath)
    check_dates(events=events_list, wait_time=args.wait_time, deadline_threshold=args.deadline)
    quit()
