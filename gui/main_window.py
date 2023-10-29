import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLabel
from PyQt5.QtCore import Qt
from utils.irig_detection import detect_irig_device, get_audio_devices

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Layout setup
        layout = QVBoxLayout()

        self.device_label = QLabel('Detected Audio Devices:')
        self.device_list = QListWidget()

        self.check_irig_button = QPushButton('Check for iRig Device')
        self.check_irig_button.clicked.connect(self.check_irig)

        layout.addWidget(self.device_label)
        layout.addWidget(self.device_list)
        layout.addWidget(self.check_irig_button)

        self.setLayout(layout)
        self.setWindowTitle('iRig Detector')

        self.load_devices()

    def load_devices(self):
        devices = get_audio_devices()
        for device in devices:
            self.device_list.addItem(f"{device[0]} - {device[1]} - {device[2]}")

    def check_irig(self):
        device_description = "iRig"  # or any other descriptor you're looking for
        is_detected = detect_irig_device(device_description)
        if is_detected:
            self.device_label.setText(f"{device_description} detected!")
        else:
            self.device_label.setText(f"{device_description} not found!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

