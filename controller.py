from event_queue import add_event, get_event, see_event_queue
from simulator import event_simulation

import time
import threading
import json
import socket


def route_event(event):
    add_event(event)


def run_simulator():

    while True:
        event = event_simulation()
        route_event(event)
        time.sleep(1)

        event = get_event()
        print(event)

# run_simulator()

# simulator_thread = threading.Thread(target=run_simulator)
# simulator_thread.start()

def convert_event(event):
    event_data = {
        "timestamp": str(event.timestamp),
        "event_type": event.event_type,
        "user": event.user,
        "ip_address": str(event.ip_address),
        "event_details": event.event_details
    }

    return event_data

# print(type(convert_event(event_simulation())))

def start_simulator():

    simulator_thread = threading.Thread(
        target=run_simulator,
        daemon=True
    )

    simulator_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nSimulator stopped.")

# start_simulator()

def json_converter():
    event = event_simulation()
    event_dict = convert_event(event)
    json_event = json.dumps(event_dict)

    return json_event

def start_server_cxn():
    HOST = "127.0.0.1"
    PORT = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print("Waiting for Blue Team...")
    connection, address = server_socket.accept()
    print("Blue Team connected:", address)

    return connection

if __name__ == "__main__":

    connection = start_server_cxn()