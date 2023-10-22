import sys
from utils.irig_detection import is_irig_like_device_connected
from utils.logging_module import initialize_logger, log_info, log_error
from utils.error_handling import DeviceDetectionError, handle_exception

# Set the global exception handler
sys.excepthook = handle_exception

def main():
    # Initialize the logger
    initialize_logger()

    log_info("Starting the application")

    try:
        # Check for iRig-like device connection
        if is_irig_like_device_connected():
            log_info("iRig-like device connected!")
            print("iRig-like device connected!")
        else:
            log_info("No iRig-like device detected.")
            print("No iRig-like device detected.")
        
        # ... other main application logic ...

    except DeviceDetectionError as e:
        log_error(f"Device Detection Error: {e}")
        print(f"Error: {e}")
    except Exception as e:
        log_error(f"Unexpected Error: {e}")
        print("An unexpected error occurred. Please check the logs or contact support.")

if __name__ == "__main__":
    main()

