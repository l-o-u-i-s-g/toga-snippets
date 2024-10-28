"""
navigating between boxes  example
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from multibox.box1 import Box1
from multibox.box2 import Box2


class multibox(toga.App):
    box1 = toga.Box()
    box2 = toga.Box()

    def startup(self):

        self.box1 = Box1(on_press=self.b1_press)
        self.box2 = Box2(on_press=self.b2_press)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.box1
        self.main_window.show()

    def b1_press(self, widget):
        self.main_window.content = self.box2

    def b2_press(self, widget):
        self.main_window.content = self.box1


def main():
    return multibox()
