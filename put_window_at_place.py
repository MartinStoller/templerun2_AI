import pygetwindow
import win32gui
import time
time.sleep(4)

hwnd = win32gui.GetForegroundWindow()

win32gui.MoveWindow(hwnd, 1200, 2, 425, 720, True)