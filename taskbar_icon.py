import os
import sys
import ctypes

def set_taskbar_icon(icon_path: str, app_id: str = "mycompany.myproduct.subproduct.version", force_window: bool = False):
    """
    Sets the taskbar icon for Windows apps using the provided .ico file.
    Works with GUI frameworks and CLI apps (with optional hidden window).

    Args:
        icon_path (str): Path to the .ico file
        app_id (str): Custom AppUserModelID for taskbar grouping
        force_window (bool): If True, creates a hidden window for CLI apps
    """
    if not os.path.exists(icon_path):
        raise FileNotFoundError(f"Icon file not found: {icon_path}")

    if sys.platform != "win32":
        return  # Only relevant on Windows

    # Set AppUserModelID for taskbar icon grouping
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
