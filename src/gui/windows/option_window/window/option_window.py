import customtkinter as ctk

from src.gui.windows.option_window.frame.button_frame import ButtonFrame
from src.gui.windows.option_window.frame.downloads_frame import DownloadsFrame
from src.gui.windows.option_window.frame.option_frame import OptionFrameWin

from src.gui.windows.option_window.widgets.radiobutt_widget import RadioButWidget

class OptionWindow(ctk.CTkToplevel):
    def __init__(self, master, core, parent_dir):
        super().__init__(master)

        self.core = core
        self.PARENT_DIR = parent_dir
        self.radio_but_widget = RadioButWidget(self)

        self.title("Налаштування")
        self.geometry("230x200")
        self.grab_set()
        self.transient(master)

        self.option_frame = OptionFrameWin(self)
        self.option_frame.pack(fill="x", padx=95)

        self.downloads_frame = DownloadsFrame(self)
        self.downloads_frame.pack(fill="x", padx=10)

        self.button_frame = ButtonFrame(self, 
                                        core=self.core,
                                        PARENT_DIR=self.PARENT_DIR,
                                        downloads_frame=self.downloads_frame)
        
        self.button_frame.pack(fill="x", padx=40, pady=10)