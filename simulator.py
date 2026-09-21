from event import Event
import random
import ipaddress


normal_event_types = [
    "LOGIN_SUCCESS",
    "LOGIN_FAILURE",
    "FILE_ACCESS",
    "SQL_QUERY"
]

def randomize_event():
    random_event = random.choice(normal_event_types)
    return random_event

users = [
    "AMINA MOHIUDEEN"
]

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


def event_simulation():
    event = Event(
    event_type= randomize_event(),
    event_details= "information",
    user= randomize_user(),
    ip_address= ip_generator(),)
    return event

inital_event = event_simulation()
print(inital_event)

