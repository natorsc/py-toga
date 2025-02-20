# -*- coding: utf-8 -*-
"""Python - Toga."""

import toga
from toga.style.pack import COLUMN, Pack

APP_ID = 'br.com.justcode.Toga'


class App(toga.App):
    def startup(self):
        vbox = toga.Box(style=Pack(direction=COLUMN, padding=12))
        scroll_container = toga.ScrollContainer(content=vbox)

        self.main_window = toga.MainWindow()
        self.main_window.content = scroll_container
        self.main_window.show()

        for button in range(1, 21):
            vbox.add(
                toga.Button(
                    text=f'Button {button}',
                )
            )


def main():
    return App(formal_name='Python Toga app', app_id=APP_ID)


if __name__ == '__main__':
    import platform

    if platform.system() == 'Windows':
        from ctypes import windll

        windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)

    main().main_loop()
