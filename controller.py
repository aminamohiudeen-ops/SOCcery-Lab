from event_queue import add_event, get_event, see_event_queue
from simulator import event_simulation

import time
import threading


def route_event(event):
    add_event(event)


def run_simulator():

    while True:
        event = event_simulation()
        route_event(event)
        time.sleep(1)
        print(see_event_queue())

# run_simulator()

simulator_thread = threading.Thread(target=run_simulator)
simulator_thread.start()