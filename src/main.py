#!/usr/bin/env python
# -*- coding: utf-8 -*-

# adapted from work by Bartlomiej "furas" Burek (https://blog.furas.pl)

import os
import tkinter
from controllers.camera_controller import CameraController
HOME = os.path.dirname(os.path.abspath(__file__))

class App:
    def __init__(self, parent, title):
        """TODO: add docstring"""

        self.parent = parent

        self.parent.title(title)
        self.parent.configure(bg="#333333")

        self.widget_controller = CameraController(root = self.parent)
        self.widget_controller.render()
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self, event=None):
        """TODO: add docstring"""

        print("[App] stopping threads")
        self.widget_controller.running = False

        print("[App] exit")
        self.parent.destroy()


if __name__ == "__main__":
    root = tkinter.Tk()
    root.configure(bg="#333333")
    root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
    App(root, "MAGIC Pose Recorder")
    root.mainloop()
