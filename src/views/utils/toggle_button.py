from tkinter import *

class ToggleButton(Canvas):
  def __init__(self, root, command=None, fg='white', bg_off='#d9dadc', bg_on='#4ED164', toggled='on', text=('On', 'Off')):
    super().__init__()
    height = 50
    width = 100
    self.bg_on = bg_on
    self.bg_off = bg_off
    self.configure(width=width, height=height,borderwidth=0, highlightthickness=0)
    self.root = root
    self.toggled = toggled
    self.label_on, self.label_off = text
    self.btn_offset = 4
    if self.toggled == 'on':
      bg = self.bg_on
      label = self.label_on
    else:
      bg = self.bg_off
      label = self.label_off

    self.left_side = self.create_arc(
        (0, 0, 0, 0), start=90, extent=180, fill=bg, outline=bg)
    self.right_side = self.create_arc(
        (0, 0, 0, 0), start=-90, extent=180, fill=bg, outline=bg)
    self.rect = self.create_rectangle(0, 0, 0, 0, fill=bg, outline=bg)
    self.btn = self.create_oval(0, 0, 0, 0, fill=fg, outline=bg)
    self.label = self.create_text(0, 0, text=label, fill='black')

    self.bind('<Configure>', self._resize)
    self.bind('<Button>', self._animate, add='+')
    self.bind('<Button>', command, add='+')

  def _animate(self, event):
    x, y, w, h = self.coords(self.btn)
    x = int(x-1)
    y = int(y-1)
    if self.toggled == 'on':
      self.moveto(self.btn, self.btn_offset, self.btn_offset)
      self.toggled = 'off'
      self._update_bg(self.bg_off)
    else:
      self.moveto(self.btn, self.coords(self.right_side)
                  [0]+self.btn_offset, self.btn_offset)
      self.toggled = 'on'
      self._update_bg(self.bg_on)

  def _update_bg(self, color):
    for bg_item in [self.left_side, self.right_side, self.rect]:
      self.itemconfig(bg_item, fill=color, outline=color)
    self.itemconfig(self.btn, outline=color)

  def _resize(self, event):
    # scale controls, in part, the y-axis placement of the button on the toggle
    scale = 5
    self.coords(self.left_side, scale, scale, event.height-scale, event.height-scale)
    self.coords(self.right_side, scale, scale, event.height, event.height-scale)
    self.coords(self.btn, scale, scale, event.height - scale, event.height-scale)
    self.coords(self.label, scale, scale)
    factor = event.width - (2*scale) - \
        (self.coords(self.right_side)[2]-self.coords(self.right_side)[0])
    self.move(self.right_side, factor, 0)
    self.coords(self.rect,
                self.bbox(self.left_side)[2]-2,
                scale,
                self.bbox(self.right_side)[0]+2,
                event.height-scale)
    self.moveto(self.label, self.coords(self.right_side)
                [2]+self.btn_offset, self.btn_offset)
    if self.toggled == 'on':
      self.moveto(self.btn, self.coords(self.right_side)
                  [0]+self.btn_offset, self.btn_offset)
    else:
      self.moveto(self.btn, self.btn_offset, self.btn_offset)

    @property
    def toggled(self):
      return self._toggled

    @toggled.setter
    def toggled(self, value):
      self._toggled = value
