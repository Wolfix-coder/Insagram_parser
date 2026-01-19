import customtkinter as ctk

from src.gui.windows.main_window.frame.directory_frame import DirectoryFrame
from src.gui.windows.main_window.frame.input_frame import InputFrame
from src.gui.windows.main_window.frame.option_frame import OptionFrame
from src.gui.windows.main_window.frame.status_bar_frame import StatusBarFrame

from src.gui.windows.main_window.widgets.log_widget import LogWidget

class MainWindow(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        core = master.core
        PARENT_DIR = master.PARENT_DIR

        self.input_frame = InputFrame(self, core, PARENT_DIR)
        self.input_frame.pack(fill="x", padx=10, pady=(20, 10))

        self.directory_frame = DirectoryFrame(self, core, PARENT_DIR)
        self.directory_frame.pack(fill="x", padx=10, pady=10)

        self.option_frame = OptionFrame(self)
        self.option_frame.pack(fill="x", padx=10, pady=10)

        self.log_frame = LogWidget(self)
        self.log_frame.pack(fill="x", padx=10, pady=10)

        self.status_bar_frame = StatusBarFrame(self, core, PARENT_DIR)
        self.status_bar_frame.pack(fill="x", padx=10, pady=10)
