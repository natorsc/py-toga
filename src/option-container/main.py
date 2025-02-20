# -*- coding: utf-8 -*-
"""Python - Toga."""

import toga
from toga.style.pack import COLUMN, Pack

APP_ID = 'br.com.justcode.Toga'


class App(toga.App):
    def startup(self):
        option_container = toga.OptionContainer(style=Pack(padding=6))

        self.main_window = toga.MainWindow()
        self.main_window.content = option_container
        self.main_window.show()

        tab1 = toga.Box(style=Pack(direction=COLUMN, padding=12))
        tab1.add(toga.Label(text='Tab1'))
        option_container.content.append('Tab1', tab1)

        tab2 = toga.Box(style=Pack(direction=COLUMN, padding=12))
        tab2.add(toga.Label(text='Tab2'))
        option_container.content.append('Tab2', tab2)


def main():
    return App(formal_name='Python Toga app', app_id=APP_ID)


if __name__ == '__main__':
    import platform

    if platform.system() == 'Windows':
        from ctypes import windll

        windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)

    main().main_loop()
