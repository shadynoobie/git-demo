from icalendar import Calendar, Event
import datetime

def create_ics_file(holidays, file_name="holidays.ics"):
    cal = Calendar()
    for date, name in holidays:
        event = Event()
        event.add('summary', name)
        event.add('dtstart', date)
        event.add('dtend', date + datetime.timedelta(days=1))  # End date is the next day
        event.add('dtstamp', datetime.datetime.now())
        cal.add_component(event)

    with open(file_name, 'wb') as f:
        f.write(cal.to_ical())

# Example input: List of tuples with (date, holiday name)
holidays = [
    (datetime.date(2025, 1, 1), "Cleo Holiday - New Year's Day"), 
    (datetime.date(2025, 12, 25), "Cleo Holiday - Christmas Day"),  
    
    (datetime.date(2025, 3, 31), "India Holiday - Eid al-Fitr"),
    (datetime.date(2025, 4, 18), "India Holiday - Baisakhi"),
    (datetime.date(2025, 5, 1), "India Holiday - May Day"),
    (datetime.date(2025, 8, 15), "India Holiday - Independence Day"),
    (datetime.date(2025, 8, 27), "India Holiday - Ganesh Chaturthi Day"),
    (datetime.date(2025, 10, 1), "India Holiday - Maha Navami"),
    (datetime.date(2025, 10, 2), "India Holiday - Vijaya Dashami"),
    (datetime.date(2025, 10, 20), "India Holiday - Diwali"),
    (datetime.date(2025, 10, 22), "India Holiday - Diwali"),
    
    (datetime.date(2025, 1, 20), "US Holiday - Martin Luther King Jr. Day"),
    (datetime.date(2025, 5, 26), "US Holiday - Memorial Day"),
    (datetime.date(2025, 6, 19), "US Holiday - Juneteenth"),
    (datetime.date(2025, 7, 4), "US Holiday - Independence Day"),
    (datetime.date(2025, 9, 1), "US Holiday - Labor Day"),
    (datetime.date(2025, 11, 27), "US Holiday - Thanksgiving"),
    (datetime.date(2025, 11, 28), "US Holiday - Thanksgiving"),
    (datetime.date(2025, 12, 24), "US Holiday - Christmas Eve"),
    
]

create_ics_file(holidays)
print("ICS file created successfully.")