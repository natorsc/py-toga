# -*- coding: utf-8 -*-
"""Python - Toga."""

import pathlib

import toga
from toga.style.pack import Pack

APP_ID = 'br.com.justcode.Toga'
HOME_DIR = pathlib.Path().home()


class App(toga.App):
    def startup(self):
        vbox = toga.Box(style=Pack(padding=12))

        self.main_window = toga.MainWindow()
        self.main_window.content = vbox
        self.main_window.show()

        button = toga.Button(text='Click me', on_press=self.on_button_pressed)
        vbox.add(button)

    async def on_button_pressed(self, widget):
        dialog = toga.OpenFileDialog('Title', HOME_DIR)

        result = await self.main_window.dialog(dialog)
        if result:
            print(result)
        else:
            print('Cancel.')


def main():
    return App(formal_name='Python Toga app', app_id=APP_ID)


if __name__ == '__main__':
    import platform

    if platform.system() == 'Windows':
        from ctypes import windll

        windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)

    main().main_loop()
