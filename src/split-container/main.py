# -*- coding: utf-8 -*-
"""Python - Toga."""

import toga
from toga.style.pack import COLUMN, Pack

APP_ID = 'br.com.justcode.Toga'


class App(toga.App):
    def startup(self):
        split_container = toga.SplitContainer(style=Pack(padding=6))

        self.main_window = toga.MainWindow()
        self.main_window.content = split_container
        self.main_window.show()

        lbox = toga.Box(style=Pack(direction=COLUMN, padding=12))
        lbox.add(toga.Label(text=f'Left Box'))

        rbox = toga.Box(style=Pack(direction=COLUMN, padding=12))
        rbox.add(toga.Label(text=f'Rigth Box'))

        split_container.content = [lbox, rbox]


def main():
    return App(formal_name='Python Toga app', app_id=APP_ID)


if __name__ == '__main__':
    import platform

    if platform.system() == 'Windows':
        from ctypes import windll

        windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)

    main().main_loop()
