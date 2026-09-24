from queue import Queue

event_queue = Queue()

event_queue.put("hello")
event_queue.put("helo")
event_queue.put("hellllo")
event_queue.put("helllllllllllo")
event_queue.put("Hello")
event_queue.put("heillo")
event_queue.put("Bye")

while not event_queue.empty():
    event = event_queue.get()
    queue = event_queue.queue
    print(queue)