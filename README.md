# SOCcery Lab

SOCcery Lab is a Python-based mini Security Operations Center (SOC) simulation designed to demonstrate how security events can be generated, transported, detected, and investigated.

The project simulates a simplified SOC workflow where normal activity is continuously generated, attacks can be launched manually, suspicious activity is detected by the Blue Team, and alerts are passed to the Purple Team for investigation and reporting.

## Project Goal

The goal of SOCcery Lab is to demonstrate the basic workflow of a SOC:

**Event Generation → Event Collection → Detection → Alert → Investigation → Incident Report**

The project is intentionally built as a local simulation rather than a real-world security monitoring system.

## Architecture

```text
                         controller.py
                              │
                    ┌─────────┴─────────┐
                    │                   │
                Simulator            Red Team
                    │                   │
                    └───────┬───────────┘
                            │
                       event_queue
                            │
                            ▼
                         server.py
                            │
                       JSON + TCP
                            │
                            ▼
                      blue_team.py
                            │
                         Detection
                            │
                            ▼
                      Purple Team
                            │
                            ▼
                   Incident Report
```

## Components

### Controller

`controller.py` acts as the main entry point for the simulation.

It:

* Starts the server
* Provides the attack menu
* Allows the user to launch attacks
* Tells the Red Team when an attack should occur

The controller does not generate events itself.

### Simulator

`simulator.py` continuously generates normal security events.

Examples include:

* Successful logins
* Failed logins
* File access
* SQL queries

Normal events are generated at regular intervals so that suspicious activity can be detected against a background of normal activity.

### Red Team

`RedTeam.py` contains the simulated attack functions.

The Red Team currently includes:

* Brute-force attack

The attacks generate security events that are placed into the same event queue as normal activity.

### Event Queue

`event_queue.py` provides a shared queue for events.

Both normal events from the Simulator and attack events from the Red Team are placed into the queue.

This allows the Server to process both types of events through the same pipeline.

### Server

`server.py` acts as the event server.

It:

1. Receives events from the shared queue
2. Converts the events into JSON
3. Sends the JSON data over a local TCP connection

The server currently uses:

```text
127.0.0.1:5000
```

### Blue Team

`blue_team.py` acts as the detection component.

It:

1. Connects to the server
2. Receives JSON events
3. Converts them back into Python data
4. Monitors the incoming events
5. Detects suspicious behaviour

The current detection rule identifies a possible brute-force attack when:

* Multiple failed logins occur
* The failures involve the same user
* The failures originate from the same IP address
* At least 5 attempts occur within a 5-second window

When the threshold is reached, the Blue Team generates an alert.

### Purple Team

`purple_team.py` receives alerts from the Blue Team.

The current Purple Team workflow:

```text
Blue Team Alert
      ↓
Purple Team
      ↓
Incident Report
```

The Purple Team currently generates an `incident_report.txt` file containing information such as:

* Alert type
* Affected user
* Source IP address
* Number of failed attempts
* Basic attack analysis

## Current Attack Workflow

The currently implemented brute-force workflow is:

```text
Red Team
   ↓
Generate LOGIN_FAILURE events
   ↓
Event Queue
   ↓
Server
   ↓
JSON
   ↓
TCP
   ↓
Blue Team
   ↓
Detect brute force
   ↓
Generate Alert
   ↓
Purple Team
   ↓
Generate incident_report.txt
```

## Technologies Used

* Python
* TCP sockets
* JSON
* Python threading
* Python queues
* Git / GitHub

## Current Features

* Continuous normal event generation
* Manual attack triggering
* Shared event queue
* Local TCP client/server communication
* JSON event transport
* Brute-force attack simulation
* Brute-force detection
* Blue Team alert generation
* Purple Team alert handling
* Automated incident report generation

## How to Run

### Requirements

* Python 3
* Git
* A terminal

No external Python packages are currently required.

### 1. Clone the repository

```bash
git clone <repository-url>
cd SOCcery-Lab
```

### 2. Start the Blue Team

Open a terminal in the project directory and run:

```bash
python blue_team.py
```

The Blue Team will attempt to connect to the local SOC server.

### 3. Start the Controller

Open a second terminal in the project directory and run:

```bash
python controller.py
```

The Controller starts the server and waits for the Blue Team to connect.

Once the connection is established, normal security events will begin flowing from the Simulator through the Server to the Blue Team.

### 4. Launch an attack

The Controller provides an attack menu.

For the currently implemented brute-force attack, select:

```text
1. Brute Force
```

Enter the number of login attempts when prompted.

The Red Team will generate the simulated failed-login events and place them into the event queue.

### 5. Observe the SOC workflow

The events will flow through the system:

```text
Simulator / Red Team
        ↓
   Event Queue
        ↓
      Server
        ↓
    JSON + TCP
        ↓
    Blue Team
        ↓
     Detection
        ↓
      Alert
        ↓
   Purple Team
        ↓
incident_report.txt
```

When the Blue Team detects the brute-force activity, the Purple Team receives the alert and generates:

```text
incident_report.txt
```

### Important

The files should be started in this order:

```text
Terminal 1:
python blue_team.py

Terminal 2:
python controller.py
```

Do **not** run `server.py` separately when using `controller.py`. The Controller starts the server as part of the SOC simulation.

The Blue Team must be running so that the Controller's server can establish the TCP connection before events are sent.


## Planned Features

Additional simulated attacks and detections will be added as the project develops.

Planned attack types include:

* Password spraying
* Suspicious file access / data discovery
* Privilege escalation
* SQL injection

Future improvements may include more detailed detection evidence and richer Purple Team incident reports.

## Disclaimer

SOCcery Lab is an educational cybersecurity simulation.

It does not perform real attacks against external systems. The simulated attacks and security events are generated locally for the purpose of demonstrating SOC concepts such as event monitoring, detection, alerting, and incident investigation.


## WTC Tracking:
WTC-BWRLPZGS

