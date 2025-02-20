# -*- coding: utf-8 -*-
"""Python - Toga."""

import toga
from toga.style.pack import COLUMN, Pack

APP_ID = 'br.com.justcode.Toga'


class App(toga.App):
    def startup(self):
        box = toga.Box(style=Pack(direction=COLUMN, padding=12))

        self.main_window = toga.MainWindow()
        self.main_window.content = box
        self.main_window.show()

        button = toga.Button(
            text='Open new window',
            on_press=self.on_button_pressed,
        )
        box.add(button)

    def on_button_pressed(self, widget):
        window = toga.Window()
        window.content = toga.Box(children=[toga.Label(text='New window.')])
        window.show()


def main():
    return App(formal_name='Python Toga app', app_id=APP_ID)


if __name__ == '__main__':
    import platform

    if platform.system() == 'Windows':
        from ctypes import windll

        windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)

    main().main_loop()
