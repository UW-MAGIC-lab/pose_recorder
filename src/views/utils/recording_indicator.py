from tkinter import *
import tkinter as tk
import tkinter.font as font

class RecordingIndicator(tk.Canvas):
  def __init__(self, parent, font_size=16):
    tk.Canvas.__init__(self, parent, borderwidth=0,
                       highlightthickness=0, bg=parent["bg"], height=30, width=150)
    self.status = 'off'
    self.show = True
    self.light = self.create_oval(0, 0, 10, 10, fill='red', outline='red')
    _, _, _, y1 = self.bbox(self.light)
    self.font = font.Font(size=font_size, family='Helvetica', weight="bold")
    self.label = self.create_text(
        (self.font.measure('Recording')), (y1-2), text='Recording', fill='white', font=self.font)
    self.pack()
    self._blink()
    self.toggle()

  def _blink(self):
    if self.show:
      if self.status == 'on':
        color = ''
        self.status = 'off'
      else:
        color = 'red'
        self.status = 'on'
      self.itemconfig(self.light, fill=color, outline=color)
      self.after(500, self._blink)

  def toggle(self):
    if self.show:
      self.itemconfig(self.light,fill='', outline='')
      self.itemconfig(self.label, text='')
    else:
      self.itemconfig(self.light, fill='red', outline='red')
      self.itemconfig(self.label, text='Recording')
    self.show = not self.show
    self._blink()
