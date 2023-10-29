import sys
from PyQt5.QtWidgets import QApplication
from utils.irig_detection import detect_irig_device
from utils.logging_module import log_info, log_error
from utils.error_handling import handle_exception
from bible_api.api_connector import BibleAPI
from gui.main_window import MainWindow  # Import the MainWindow class

# Set the global exception handler
sys.excepthook = handle_exception

def main():
    log_info("Starting the application")

    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

        # This code below won't be reached unless the GUI is closed, 
        # but you can keep or move some of it to the GUI event handlers
        if detect_irig_device("iRig Pre HD"):
            log_info("iRig-like device connected!")
            print("iRig-like device connected!")

            # Example usage: Fetch a verse when an iRig-like device is detected
            result = BibleAPI.fetch_verse("John 3:16")
            if result:
                log_info(f"Fetched verse: {result['text']}")
                print(result['text'])
        else:
            log_info("No iRig-like device detected.")
            print("No iRig-like device detected.")

        # ... other main application logic ...

    except Exception as e:
        log_error(f"Unexpected Error: {e}")
        print("An unexpected error occurred. Please check the logs or contact support.")

if __name__ == "__main__":
    main()
