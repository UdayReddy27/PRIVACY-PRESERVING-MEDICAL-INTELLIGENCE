import time
import logging
import datetime
from .utils import logger
from .core import user_auth

FAILED_LOGIN_THRESHOLD = 3
LOGIN_ATTEMPT_WINDOW = 60  # seconds
SUSPICIOUS_ACCESS_TIME = (0, 6)  # 12:00 AM to 6:00 AM

failed_login_attempts = {}  # {username: [timestamps]}

def detect_suspicious_login(username, password):
    """
    Detects suspicious login behavior such as repeated failed logins.

    Args:
        username (str): The username attempting to log in.
        password (str): The password entered.

    Returns:
        bool: True if suspicious behavior is detected, False otherwise.
    """
    global failed_login_attempts
    now = time.time()

    if username not in failed_login_attempts:
        failed_login_attempts[username] = []

    # Remove old attempts
    failed_login_attempts[username] = [ts for ts in failed_login_attempts[username] if now - ts < LOGIN_ATTEMPT_WINDOW]

    if not user_auth.authenticate_user(username, password):
        failed_login_attempts[username].append(now)
        num_attempts = len(failed_login_attempts[username])
        if num_attempts >= FAILED_LOGIN_THRESHOLD:
            # Use integer value 30 for WARNING
            logger.log_message(f"Intrusion detected: {username} has {num_attempts} failed login attempts within {LOGIN_ATTEMPT_WINDOW} seconds.", level=30)
            return True
        else:
            # Use integer value 20 for INFO
            logger.log_message(f"{username} has {num_attempts} failed login attempts.", level=20)
            return False
    else:
        # Reset attempts on successful login
        failed_login_attempts[username] = []
        return False

def detect_unusual_access_time():
    """
    Detects if the current access time is unusual (e.g., outside business hours).

    Returns:
        bool: True if the access time is unusual, False otherwise.
    """
    now = datetime.datetime.now()
    hour = now.hour
    if SUSPICIOUS_ACCESS_TIME[0] <= hour <= SUSPICIOUS_ACCESS_TIME[1]:
        # Use integer value 30 for WARNING
        logger.log_message(f"Intrusion detected: Unusual access time at {now.strftime('%H:%M')}.", level=30)
        return True
    return False

if __name__ == '__main__':
    # Example Usage
    username = "testuser"
    password = "wrongpassword"

    for i in range(4):
        is_suspicious = detect_suspicious_login(username, password)
        if is_suspicious:
            print("Suspicious login detected!")
        time.sleep(15)

    if detect_unusual_access_time():
        print("Unusual access time detected!")
