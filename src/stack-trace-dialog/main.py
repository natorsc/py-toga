# -*- coding: utf-8 -*-
"""Python - Toga."""

import toga
from toga.style.pack import Pack

APP_ID = 'br.com.justcode.Toga'


PRE_FORMATTED = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad 
minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat 
cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
laborum.
"""


class App(toga.App):
    def startup(self):
        vbox = toga.Box(style=Pack(padding=12))

        self.main_window = toga.MainWindow()
        self.main_window.content = vbox
        self.main_window.show()

        button = toga.Button(text='Click me', on_press=self.on_button_pressed)
        vbox.add(button)

    async def on_button_pressed(self, widget):
        dialog = toga.StackTraceDialog(
            'Title',
            'Dialog text.',
            PRE_FORMATTED,
        )
        await self.main_window.dialog(dialog)


def main():
    return App(formal_name='Python Toga app', app_id=APP_ID)


if __name__ == '__main__':
    import platform

    if platform.system() == 'Windows':
        from ctypes import windll

        windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)

    main().main_loop()
