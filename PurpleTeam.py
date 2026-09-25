def receive_alert(alert):
    generate_report(alert)


def generate_report(alert):
    report = f"""
SECURITY INCIDENT REPORT

Alert Type: {alert["alert_type"]}
User: {alert["user"]}
Source IP: {alert["ip_address"]}
Failed Attempts: {alert["failed_attempts"]}

Analysis:
A possible brute-force attack was detected.
Multiple failed login attempts were made against the same user
from the same source IP within a short period of time.

"""

    with open("incident_report.txt", "w") as file:
        file.write(report)