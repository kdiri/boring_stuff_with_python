"""
.. module:: controll_gui.mouse_controll
   :synopsis: move, click, drag mouse
"""
import pyautogui
import time


# If you're having problem on OS X:
# https://www.reddit.com/r/inventwithpython/comments/f6nepq/issues_with_pyautoguidrag/


def drag_mouse(ss=False):
    time.sleep(3)
    distance = 300
    change = 20
    while distance > 0:
        pyautogui.drag(distance, 0, duration=0.2, button="left")  # right
        distance -= change
        pyautogui.drag(0, distance, duration=0.2, button="left")  # down
        pyautogui.drag(-distance, 0, duration=0.2, button="left")  # left
        distance -= change
        pyautogui.drag(0, -distance, duration=0.2, button="left")  # up
    if ss:
        take_screenshot()


def take_screenshot():
    pyautogui.screenshot()


if __name__ == "__main__":
    drag_mouse(ss=True)
