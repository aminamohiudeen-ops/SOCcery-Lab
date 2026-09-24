from event import Event
from queue import Queue

event_queue = Queue()

def add_event(event):
    event_queue.put(event)

def get_event():
    return event_queue.get()

def see_event_queue():
    return event_queue.queue

# print(see_event_queue())

# test_event = Event(
#     event_type="LOGIN_SUCCESS",
#     user="AMINA MOHIUDEEN",
#     ip_address="10.200.131.10",
#     event_details="successful login"
# )

# event_queue.put(test_event)
# event = event_queue.get()

# queue = event_queue.queue

# print(queue)
# print(event)