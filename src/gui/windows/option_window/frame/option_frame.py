import customtkinter as ctk

from utils.logging import get_logger

logger = get_logger("OPT_FRAME")

class OptionFrameWin(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        self.label_option = ctk.CTkLabel(self, text="Option")
        self.label_option.grid(row=0, column=0, sticky="w")

        