from datetime import datetime
class Event:
    def __init__(self, event_type, user, ip_address, event_details):

        self.timestamp = datetime.now()
        self.event_type = event_type.upper()
        self.user = user.lower()
        self.ip_address = ip_address
        self.event_details = event_details
    
    def __str__(self):
        return f"{self.timestamp} {self.event_type} user={self.user} ip={self.ip_address} details={self.event_details}"

# print(date_time) 
event = Event(
    event_type= "Successful login",
    event_details= "information",
    user= "Amina Mohiudeen",
    ip_address= "10.200.131.93",   
)

event2 = Event(
    event_type= "file accsess",
    event_details= "information",
    user = "Amina",
    ip_address= "10.200.131.93",
)

print(event)
print(event2)