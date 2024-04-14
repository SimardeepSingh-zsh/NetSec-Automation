# security_logging.py

import logging

def log_security_event(event):
    logging.info(f"Security event: {event}")

if __name__ == "__main__":
    logging.basicConfig(filename="security_events.log", level=logging.INFO)
    log_security_event("Unauthorized access detected")
