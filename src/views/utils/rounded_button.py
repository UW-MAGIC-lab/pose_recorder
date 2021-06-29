from tkinter import *
import tkinter as tk
import tkinter.font as font

class RoundedButton(tk.Canvas):
  def __init__(self, parent, border_radius, padding, color, text='', command=None, enabled=True):
    tk.Canvas.__init__(self, parent, borderwidth=0,
                       relief="flat", highlightthickness=0, bg=parent["bg"])
    self.command = command
    font_size = 16
    self.font = font.Font(size=font_size, family='Helvetica', weight="bold")
    self.id = None
    self.enabled = True
    self.color = color
    self.padding = padding
    self.border_radius = border_radius
    height = font_size+(2*padding)
    width = self._calculate_width(text)
    width = width if width >= 80 else 80

    if border_radius > 0.5*width:
      print("Error: border_radius is greater than width.")
      return None

    if border_radius > 0.5*height:
      print("Error: border_radius is greater than height.")
      return None


    def shape():
      rad = 2*self.border_radius
      id_1 = self.create_arc((0, rad, rad, 0),
                      start=90, extent=90, fill=color, outline=color)
      id_2 = self.create_arc((width-rad, 0, width,
                        rad), start=0, extent=90, fill=color, outline=color)
      id_3 = self.create_arc((width, height-rad, width-rad,
                        height), start=270, extent=90, fill=color, outline=color)
      id_4 = self.create_arc((0, height-rad, rad, height), start=180, extent=90, fill=color, outline=color)
      id_5 = self.create_polygon((0, height-border_radius, 0, border_radius, border_radius, 0, width-border_radius, 0, width,
                           border_radius, width, height-border_radius, width-border_radius, height, border_radius, height), fill=color, outline=color)
      return (id_1, id_2, id_3, id_4, id_5)

    self.id = shape()
    (x0, y0, x1, y1) = self.bbox("all")
    width = (x1-x0)
    height = (y1-y0)
    self.configure(width=width, height=height)
    self.text_id = self.create_text(width/2, height/2,text=text, fill='white', font= self.font)
    self.bind("<ButtonPress-1>", self._on_press)
    self.bind("<ButtonRelease-1>", self._on_release)
    if not enabled:
      self.disable()

  def disable(self):
    for id in self.id:
      self.itemconfigure(id, fill='gray', outline='gray')
    self.enabled = False

  def enable(self):
    for id in self.id:
      self.itemconfigure(id, fill=self.color, outline=self.color)
    self.enabled = True

  def _on_press(self, event):
      self.configure(relief="sunken")

  def _on_release(self, event):
      self.configure(relief="raised")
      if self.command is not None and self.enabled:
          self.command()

  def _calculate_width(self, text):
    return self.font.measure(text)+(4*self.padding)
