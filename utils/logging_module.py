import logging
import os
from datetime import datetime

# Ensure logs directory exists
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Define log file path
log_file = os.path.join(log_dir, 'app.log')

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s]: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.FileHandler(log_file),
                              logging.StreamHandler()])

def log_info(message: str):
    """Logs an info message."""
    logging.info(message)

def log_error(message: str):
    """Logs an error message."""
    logging.error(message)

def log_debug(message: str):
    """Logs a debug message."""
    logging.debug(message)

def compute_time(func):
    """
    Decorator to compute and log the execution time of a function.
    
    Args:
        func (function): The function to be wrapped.
        
    Returns:
        function: The wrapped function.
    """
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        elapsed_time = (end_time - start_time).total_seconds()
        log_info(f"{func.__name__} executed in {elapsed_time} seconds.")
        return result

    return wrapper

