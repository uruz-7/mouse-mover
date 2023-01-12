from time import sleep
import pyautogui
import numpy as np


class Move:
    def __init__(self, top_left=1, top_right=pyautogui.size().width, bottom_left=1, bottom_right=pyautogui.size().height, interval=10, smooth_move=True):
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.interval = interval
        self.smooth_move = smooth_move

    def move(self):

        while True:
            # Get the position of the mouse cursor
            pos1 = pyautogui.position()
            sleep(self.interval)
            pos2 = pyautogui.position()
            if pos2 != pos1:
                continue

            self.auto_move()

    def auto_move(self):
        x = np.random.randint(self.top_left, self.top_right)
        y = np.random.randint(self.bottom_left, self.bottom_right)

        print("Moving to (%d, %d)" % (x, y))
        pyautogui.moveTo(x, y, duration=0.5)
