from event import Event
import random
import ipaddress
import time
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
    hosts_range = hosts[:20]
    random_ip = random.choice(hosts_range)
    return random_ip

attempts = int(input("Input the amount of attempts:"))
user = randomize_user()
ip_address = ip_generator()
def brute_force(user, ip_address, attempts):
    # brute_list = []

    while attempts > 0:
        # while len(brute_list) < attempts:
        brute_event = Event(
        event_type= "LOGIN_FAILURE",
        event_details= "",
        user= user,
        ip_address= ip_address,)

        yield brute_event
        attempts -= 1
        # brute_list.append(brute_event)

        time.sleep(1)    

    # return brute_list
    
for event in brute_force(user, ip_address, attempts):
    print(event)
