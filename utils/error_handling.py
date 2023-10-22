from utils.logging_module import log_error, log_debug

# Custom Exception Classes
class DeviceDetectionError(Exception):
    """Exception raised for errors in the device detection."""

class LoggingError(Exception):
    """Exception raised for errors during logging."""

# ... You can add more custom exceptions as your application grows ...

def handle_exception(exc_type, exc_value, traceback):
    """
    Global exception handler.
    Logs the exception and provides a user-friendly message.
    """
    log_error(f"{exc_type.__name__}: {exc_value}")
    if isinstance(exc_value, DeviceDetectionError):
        print(f"Error: {exc_value}")
    elif isinstance(exc_value, LoggingError):
        print(f"Logging Error: {exc_value}")
    else:
        print("An unexpected error occurred. Please check the logs or contact support.")
    
    # If in debug mode, print the traceback
    log_debug(traceback)

# To use this as the global exception handler:
# import sys
# sys.excepthook = handle_exception
