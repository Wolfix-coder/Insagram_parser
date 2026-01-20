import customtkinter as ctk

from utils.logging import GUIHandler

class LogWidget (ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        self.log_text_box = ctk.CTkTextbox(self, width=550, height=175)
        self.log_text_box.grid(row=0, column=0, padx=15)

        # Підключаємо textbox до всіх logger'ів
        GUIHandler.set_textbox(self.log_text_box)
