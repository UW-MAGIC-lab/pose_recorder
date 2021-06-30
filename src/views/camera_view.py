import PIL.ImageTk
import tkinter
from tkinter import font
from tkinter import ttk
from views.utils.rounded_button import RoundedButton
from views.utils.recording_indicator import RecordingIndicator

class CameraView(tkinter.Frame):

  def __init__(self, parent, fps=""):
    """
      Main Camera View
    """
    super().__init__(parent)
    # need to update in order to get access to parent's width & height
    self.update()
    bg = parent["bg"]
    self["bg"] = bg
    self.parent = parent
    self.width = parent.winfo_width()
    self.height = parent.winfo_height()
    self.fps = fps
    self.filename = None
    self.menu_font = font.Font(family='Helvetica', size=18, weight='bold')

    self._draw_control_panel(bg)
    self._draw_left_menu(bg)
    self.right_menu = tkinter.Frame(self, width=self.width*0.2, bg=bg)
    self._draw_status_bar()
    self.canvas_area = tkinter.Canvas(self, width=self.width*0.6, height=self.height * 0.8, bg=bg)
    self._arrange_view_grid()
    # row/column configure are necessary to make the widget fill the entire space of the container
    # TODO: extract ViewFrame into own class, have CameraView inherit from ViewFrame
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure(2, weight=1)
    self.grid_rowconfigure(0, weight=1)
    self.grid_rowconfigure(1, weight=1)
    self.grid_rowconfigure(2, weight=1)
    self.grid_rowconfigure(3, weight=1)

  def update_canvas(self, frame):
    self.photo = PIL.ImageTk.PhotoImage(image=frame)
    self.canvas_area.create_image(0, 0, image=self.photo, anchor='nw')

  def update_directory(self):
    self.status_dir.configure(text = f'Save to: {self.filename}')

  def _draw_status_bar(self):
    self.status_frame = tkinter.Frame(self, height=self.height * 0.2)
    self.status = tkinter.Label(self.status_frame, text='')
    self.status.pack(side='left')

  def _draw_left_menu(self, bg):
    self.left_menu = tkinter.Frame(self, width=self.width*0.2, bg=bg)
    self.recording_indicator = RecordingIndicator(self.left_menu)

    self.select_dir_btn = RoundedButton(
        self.left_menu, border_radius=3, padding=8, color="#4986E7", text='Save As')
    self.select_dir_btn.pack(anchor='nw')

    self.start_btn = RoundedButton(
        self.left_menu, border_radius=3, padding=8, color="#16A765", text='Start Camera', enabled=False)
    self.start_btn.pack(anchor='nw')

    self.stop_btn = RoundedButton(
        self.left_menu, border_radius=3, padding=8, color="#FA573C", text='Stop Camera', enabled=False)
    self.stop_btn.pack(anchor='nw')

    self.start_record_btn = RoundedButton(
        self.left_menu, border_radius=3, padding=8, color="#7BD148", text='Start Recording', enabled=False)
    self.start_record_btn.pack(anchor='nw')
    self.stop_record_btn = RoundedButton(
        self.left_menu, border_radius=3, padding=8, color="#FF7537", text='Stop Recording', enabled=False)
    self.stop_record_btn.pack(anchor='nw')


  def _arrange_view_grid(self):
    self.left_menu.grid(row=0, column=0, rowspan=2,
                        sticky="nsew", pady=(self.height*0.08, 0), padx=16)
    self.right_menu.grid(row=0, column=2, rowspan=2,
                         sticky="nsew")
    self.canvas_area.grid(row=1, column=1, sticky="nsew")
    self.status_frame.grid(row=2, column=0, columnspan=3,
                           rowspan=2, sticky="sew")

  def _draw_control_panel(self, bg):
    self.controls = tkinter.Frame(self, width=self.width*0.6, height=self.height * 0.2, bg=bg, pady=8)
    self.controls.grid(row=0, column=1, sticky="ew")
    self.status_dir = tkinter.Label(
        self.controls, fg='white', justify="left", bg=bg,
        font=self.menu_font, pady=8, padx=8)
    self.update_directory()
    self.status_dir.pack(side='left')
    self.status_fps = tkinter.Label(
        self.controls, fg='white', wraplength=300, justify="left",
        text=f'FPS:{self.fps}', bg=bg,
        font=self.menu_font, pady=8, padx=8)
    self.status_fps.pack(side='right')
