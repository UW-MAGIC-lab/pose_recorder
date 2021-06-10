import PIL.ImageTk
import tkinter
from tkinter import font
from tkinter import ttk
from views.utils.rounded_button import RoundedButton

class CameraView(tkinter.Frame):

  def __init__(self, parent, fps=""):
    """
      Main Camera View
    """
    super().__init__(parent)
    bg = parent["bg"]
    self["bg"] = bg
    self.width = parent.winfo_screenwidth()
    self.height = parent.winfo_screenheight()
    self.fps = fps
    self.filename = None

    self._draw_control_panel(bg)
    self._draw_left_menu(bg)
    self.right_menu = tkinter.Frame(self, width=self.width*0.2, bg=bg)
    self._draw_status_bar()
    self.canvas_area = tkinter.Canvas(self, width=self.width*0.6, height=self.height * 0.8, bg=bg)
    self._arrange_view_grid()

  def update_canvas(self, frame):
    self.photo = PIL.ImageTk.PhotoImage(image=frame)
    self.canvas_area.create_image(0, 0, image=self.photo, anchor='nw')

  def update_directory(self):
    self.status_dir.configure(text = f'Save to:\n\n {self.filename}')

  def _draw_status_bar(self):
    self.status_frame = tkinter.Frame(self, height=self.height * 0.2)
    self.status = tkinter.Label(self.status_frame, text='')
    self.status.pack(side='left')

  def _draw_left_menu(self, bg):
    menu_font = font.Font(family='Helvetica', size=18, weight='bold')
    self.left_menu = tkinter.Frame(self, width=self.width*0.2, bg=bg)
    self.status_fps = tkinter.Label(
        self.left_menu, fg='white', wraplength=300, justify="left",
        text=f'FPS:{self.fps}', bg=bg,
        font=menu_font, pady=8)
    self.status_fps.pack(anchor='nw')
    self.select_dir_btn = RoundedButton(
        self.left_menu, border_radius=3, padding=8, color="#4986E7", text='Save File')
    self.select_dir_btn.pack(anchor='nw')
    self.status_dir = tkinter.Label(
      self.left_menu, fg='white', wraplength=300, justify="left",bg=bg,
      font=menu_font, pady=8)
    self.update_directory()
    self.start_record_btn = RoundedButton(
        self.left_menu, border_radius=3, padding=8, color="#7BD148", text='Start Recording')
    self.start_record_btn.pack(anchor='n')
    # self.start_record_btn.itemconfigure(state='hidden')
    self.stop_record_btn = RoundedButton(
        self.left_menu, border_radius=3, padding=8, color="#FF7537", text='Stop Recording')
    self.stop_record_btn.pack(anchor='n')
    # self.stop_record_btn.itemconfigure(state='hidden')
    self.status_dir.pack(anchor='nw')




  def _arrange_view_grid(self):
    self.left_menu.grid(row=0, column=0, rowspan=2,
                        sticky="nsew", pady=(self.height*0.08, 0), padx=16)
    self.right_menu.grid(row=0, column=2, rowspan=2,
                         sticky="nsew")
    self.canvas_area.grid(row=1, column=1, sticky="nsew")
    self.status_frame.grid(row=2, column=0, columnspan=3,
                           rowspan=2, sticky="ew")

  def _draw_control_panel(self, bg):
    self.controls = tkinter.Frame(self, width=self.width*0.6, height=self.height * 0.2, bg=bg, pady=8)
    self.controls.grid(row=0, column=1, sticky="ew")

    self.start_btn = RoundedButton(
        self.controls, border_radius=3, padding=8, color="#16A765", text='Start Camera')
    self.start_btn.pack( side='left')

    self.stop_btn = RoundedButton(
        self.controls, border_radius=3, padding=8, color="#FA573C", text='Stop Camera')
    self.stop_btn.pack( side='left')
