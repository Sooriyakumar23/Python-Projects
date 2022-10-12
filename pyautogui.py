import pyautogui
import time

time.sleep(2)

count = 1

while count <= 1000:
    pyautogui.typewrite("Hi, I am Sooriyakumar " + str(count))
    pyautogui.press("enter")
    count += 1