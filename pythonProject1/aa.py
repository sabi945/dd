import pyautogui

# Buka aplikasi "Notepad"
pyautogui.hotkey("win", "r")
pyautogui.write("notepad")
pyautogui.press("enter")

# Masukkan teks "Hello World"
pyautogui.write("Hello World")
