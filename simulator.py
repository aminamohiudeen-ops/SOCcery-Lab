from event import Event
import random
def event_simulation():
    event = Event(
    event_type= "Successful login",
    event_details= "information",
    user= "Amina Mohiudeen",
    ip_address= "10.200.131.93",)

    return event

inital_event = event_simulation()
print(inital_event)

