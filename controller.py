import threading
from server import start_server_cxn, send_events
from RedTeam import brute_force, randomize_user, ip_generator
from event_queue import add_event

blue_team_connected = False

def start_server():
    global blue_team_connected
    connection = start_server_cxn()
    blue_team_connected = True
    send_events(connection)


server_thread = threading.Thread(
    target=start_server,
    daemon=True
)

server_thread.start()

def launch_brute_force():
    user = randomize_user()
    ip_address = ip_generator()

    for event in brute_force(user, ip_address):
        add_event(event)


def attack_menu():
    while not blue_team_connected:
        pass

    while True:
        choice = input("\n1. Brute Force\n Select attack: ")

        if choice == "1":
            launch_brute_force()
        print("\nAttack Deployed Successfully\n")

if __name__ == "__main__":
    
    attack_menu()

