import os
import platform
from utils.logging_module import log_info, log_debug

def get_audio_devices():
    """
    Fetch audio devices on a Windows system using WMI.

    Returns:
    - list: A list of tuples containing name, description, and status of each device.
    """
    try:
        import win32com.client
        wmi = win32com.client.GetObject("winmgmts:")
        devices = wmi.InstancesOf("Win32_SoundDevice")
        device_list = []
        for device in devices:
            name = device.Name
            description = device.Description
            status = device.Status
            device_list.append((name, description, status))
        return device_list
    except ImportError:
        log_info("win32com module not available on this platform.")
        return []
    except Exception as e:
        log_info(f"Error fetching audio devices: {e}")
        return []

def detect_irig_device(device_description):
    """
    Check for the presence of an iRig (or similar) device based on a description.

    Parameters:
    - device_description (str): Description or name of the device to be detected.

    Returns:
    - bool: True if device is detected, otherwise False.
    """
    os_type = platform.system()
    devices = []

    if os_type == "Windows":
        devices = get_audio_devices()
        for device in devices:
            if device_description in device[0] or device_description in device[1]:
                log_info(f"Device '{device_description}' detected!")
                return True
    elif os_type in ["Linux", "Darwin"]:  # Linux and macOS
        devices_output = os.popen('ls /dev/').read()
        devices = devices_output.split("\n")
    else:
        log_info(f"Unsupported OS type: {os_type}")
        return False

    log_debug(f"Connected devices on {os_type}: {devices}")

    if any(device_description in device for device in devices):
        log_info(f"Device '{device_description}' detected!")
        return True
    else:
        log_info(f"Device '{device_description}' not found.")
        return False


