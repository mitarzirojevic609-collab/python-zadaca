import subprocess
import webbrowser
import win10toast
from pyexpat.errors import messages
from win10toast import ToastNotifier
import time
import random
import threading

toaster = ToastNotifier()


messages = [
    "take a break"
    "it s time to chill"
    "life is good"
    "ti si radna masinaaa"
]

subprocess.Popen(["C:/Program Files/JetBrains/PyCharm 2025.3.2.1/bin/pycharm.exe"])
webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://itskola.net")


def show_notification():
    while True:
        toaster.show_toast("Reminder!", random.choice(messages),duration=5)
        time.sleep(5)

sn_thread = threading.Thread(target=show_notification)
sn_thread.start()


print("hello world")


