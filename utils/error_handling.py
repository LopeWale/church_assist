from utils.logging_module import log_error, log_debug

# Custom Exception Classes

class DeviceDetectionError(Exception):
    """Exception raised for errors in the device detection."""

class LoggingError(Exception):
    """Exception raised for errors during logging."""

class APIConnectionError(Exception):
    """Exception raised for errors connecting to the Bible API."""

class APIResponseError(Exception):
    """Exception raised for unexpected responses from the Bible API."""

# ... You can add more custom exceptions as your application grows ...

def handle_exception(exc_type, exc_value, traceback):
    """
    Global exception handler.
    Logs the exception and provides a user-friendly message.
    """
    log_error(f"{exc_type.__name__}: {exc_value}")

    # Device Detection Error
    if isinstance(exc_value, DeviceDetectionError):
        print(f"Error: {exc_value}")

    # Logging Error
    elif isinstance(exc_value, LoggingError):
        print(f"Logging Error: {exc_value}")

    # API Connection Error
    elif isinstance(exc_value, APIConnectionError):
        print(f"API Connection Error: {exc_value}")

    # API Response Error
    elif isinstance(exc_value, APIResponseError):
        print(f"API Response Error: {exc_value}")

    # Generic unexpected error
    else:
        print("An unexpected error occurred. Please check the logs or contact support.")
    
    # If in debug mode, print the traceback (consider refining this part based on how you want to handle debug information)
    log_debug(traceback)
