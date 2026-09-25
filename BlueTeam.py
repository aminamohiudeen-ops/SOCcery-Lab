import socket
import json
from datetime import datetime

failed_logins = []
matching_failures = []
def start_client_cxn():
    HOST = "127.0.0.1"
    PORT = 5000
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((HOST,PORT))
    client_file = client_socket.makefile("r")

    for line in client_file:
        event = json.loads(line)
        print(event)
        if event["event_type"] == "LOGIN_FAILURE":
            brute_force_detection(event)
            failed_logins.append(event)
            print(f"Failed logins tracked: {len(failed_logins)}")

    while True:

        message = client_socket.recv(1024)
        if not message:
            break

        print(message.decode())

def brute_force_detection(event):

    matching_failures.clear()

    current_time = datetime.fromisoformat(event["timestamp"])

    for failure in failed_logins:

        if (
            event["user"] == failure["user"]
            and event["ip_address"] == failure["ip_address"]
        ):

            failure_time = datetime.fromisoformat(failure["timestamp"])

            time_difference = (
                current_time - failure_time
            ).total_seconds()

            if time_difference <= 5:
                matching_failures.append(failure)

    if len(matching_failures) >= 4:
        print("\n \n \n !!POSSIBLE BRUTE FORCE ATTACK DETECTED!! \n \n \n")
        print(
            f"User: {event['user']} | "
            f"IP: {event['ip_address']} | "
            f"Failed attempts: {len(matching_failures) + 1}"
        )

            
        
  

if __name__ == "__main__":
    start_client_cxn()
