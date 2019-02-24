class Event:

    def __init__(self):
        self._date = None
        self._event_type = None
        self._person_name = None
        self._description = None
    
    def __str__(self):
        return ("Event Type:        %s\n" 
                "Date:              %s\n"
                "Person Name:       %s\n"    
                "Description:       %s\n"
                % (self._event_type, self._date, self._person_name, self._description)
        )

    def date(self,date):
        self._date = date
        return self
    
    def person_name(self, person_name):
        self._person_name = person_name
        return self
    
    def event_type(self, event_type):
        self._event_type = event_type
        return self

    def description(self, description):
        self._description = description
        return self

    def days_to_deadline(self, today):
        date_diff = self._date - today
        return date_diff.days