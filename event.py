from datetime import datetime
class Event:
    def __init__(self, event_type, user, ip_address, event_details):

        self.timestamp = datetime.now()
        self.event_type = event_type
        self.user = user
        self.ip_address = ip_address
        self.event_details = event_details

date_time = datetime.now()
# print(date_time) 
event = Event(
    event_type= "Attack",
    event_details= "information",
    user= "Amina Mohiudeen",
    ip_address= "10.200.131.93",   
)

print(event.timestamp)