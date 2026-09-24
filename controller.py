from event import Event
from queue import Queue

event_queue = Queue()

test_event = Event(
    event_type="LOGIN_SUCCESS",
    user="AMINA MOHIUDEEN",
    ip_address="10.200.131.10",
    event_details="successful login"
)

event_queue.put(test_event)
event = event_queue.get()

queue = event_queue.queue

print(queue)
print(event)