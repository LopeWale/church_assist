import os
import platform
from utils.logging_module import log_info, log_debug

try:
    import win32com.client
except ImportError:
    pass  # This module is available only for Windows

def get_audio_devices():
    wmi = win32com.client.GetObject("winmgmts:")
    devices = wmi.InstancesOf("Win32_SoundDevice")
    device_list = []
    for device in devices:
        name = device.Name
        description = device.Description
        status = device.Status
        device_list.append((name, description, status))
    return device_list

def detect_irig_device(device_description):
    """
    Check for the presence of an iRig (or similar) device based on a description.

    Parameters:
    - device_description (str): Description or name of the device to be detected.

    Returns:
    - bool: True if device is detected, otherwise False.
    """
    os_type = platform.system()

    if os_type == "Windows":
        devices = get_audio_devices()
        for device in devices:
            if device_description in device[0] or device_description in device[1]:
                log_info(f"Device '{device_description}' detected!")
                return True
    elif os_type == "Linux":
        devices = os.popen('ls /dev/').read()
    elif os_type == "Darwin":  # macOS
        devices = os.popen('ls /dev/').read()
    else:
        log_info(f"Unsupported OS type: {os_type}")
        return False

    log_debug(f"Connected devices on {os_type}: {devices}")

    if device_description in devices:
        log_info(f"Device '{device_description}' detected!")
        return True
    else:
        log_info(f"Device '{device_description}' not found.")
        return False

# Sample usage
if __name__ == "__main__":
    detect_irig_device("iRig Pre HD")

