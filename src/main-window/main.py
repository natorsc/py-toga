# -*- coding: utf-8 -*-
"""Python - Toga."""

import toga

APP_ID = 'br.com.justcode.Toga'


class App(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow()
        self.main_window.show()


def main():
    return App(formal_name='Python Toga app', app_id=APP_ID)


if __name__ == '__main__':
    import platform

    if platform.system() == 'Windows':
        from ctypes import windll

        windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)

    main().main_loop()
