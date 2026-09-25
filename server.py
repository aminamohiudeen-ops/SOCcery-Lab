import threading
import socket
import json
from event_queue import get_event
from simulator import run_simulator


def convert_event(event):
    event_data = {
        "timestamp": str(event.timestamp),
        "event_type": event.event_type,
        "user": event.user,
        "ip_address": str(event.ip_address),
        "event_details": event.event_details
    }

    return event_data

def json_converter(event):
    
    event_dict = convert_event(event)
    json_event = json.dumps(event_dict)

    return json_event

def start_server_cxn():
    HOST = "127.0.0.1"
    PORT = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print("Waiting for Blue Team...\n")
    connection, address = server_socket.accept()
    print("Blue Team connected:", address)

    simulator_thread = threading.Thread(
    target=run_simulator,
    daemon=True
)

    simulator_thread.start()

  

    return connection

def send_events(connection):
    while True:
            event = get_event()
            json_event = json_converter(event)
    
            connection.sendall((json_event + "\n").encode())

if __name__ == "__main__":

    connection = start_server_cxn()
    send_events(connection)