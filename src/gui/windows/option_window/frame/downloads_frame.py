import customtkinter as ctk

from src.gui.windows.option_window.widgets.radiobutt_widget import RadioButWidget

class DownloadsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        self.label_download = ctk.CTkLabel(self, text="Downloads:")
        self.label_download.grid(row=0, column=0, sticky="w", padx=10)

        self.radio_but_widget = RadioButWidget(self)
        self.radio_but_widget.grid(row=1, column=0)