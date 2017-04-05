"""Helper Functions"""

from datetime import datetime

def get_timestamp():
    """Get current timestamp."""

    current_time = datetime.now()
    return current_time.strftime('%Y-%m-%d %H:%M:%S')