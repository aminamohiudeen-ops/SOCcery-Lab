from event import Event
import random
import ipaddress
import time

normal_event_types = [
    "LOGIN_SUCCESS",
    "LOGIN_FAILURE",
    "FILE_ACCESS",
    "SQL_QUERY"
]

normal_event_details = {
    "LOGIN_SUCCESS": [
        "successful login",
        "user authenticated",
        "login accepted"
    ],

    "LOGIN_FAILURE": [
        "incorrect password",
        "invalid credentials",
        "authentication failed"
    ],

    "FILE_ACCESS": [
        "opened payroll.xlsx",
        "accessed report.pdf",
        "read employee_data.csv"
    ],

    "SQL_QUERY": [
        "SELECT * FROM users",
        "SELECT * FROM transactions",
        "SELECT username FROM accounts"
    ]
}

users = [
    "AMINA MOHIUDEEN"
]

def randomize_event():
    random_event = random.choice(normal_event_types)
    return random_event

def randomize_user():
    random_user = random.choice(users)
    return random_user

def ip_list_generator():
    network = ipaddress.ip_network("10.200.131.0/24")
    # random_ip = random.choice(list(network.hosts()))
    ip_list = list(network.hosts())
    return ip_list

def ip_generator():
    hosts = ip_list_generator()
    hosts_range = hosts[:10]
    random_ip = random.choice(hosts_range)
    return random_ip

def randomize_event_details(event_type):

    if event_type in normal_event_details:
        details = normal_event_details[event_type]
        return random.choice(details)

def event_simulation():
    eventType = randomize_event()
    event = Event(
    event_type= eventType,
    event_details= randomize_event_details(eventType),
    user= randomize_user(),
    ip_address= ip_generator(),)

    return event

# inital_event = event_simulation() 
# # print(inital_event)

# def run_simulation():
#     while True:
#         event = event_simulation()
#         print(event)
#         time.sleep(1)

# if __name__ == "__main__":
#     run_simulation()

