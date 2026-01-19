import customtkinter as ctk

class StatusWidget (ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        self.progress_bar = ctk.CTkProgressBar(self, width=350, orientation="horizontal")
        self.progress_bar.grid(row=0, column=0, sticky="ew", padx=(30, 15))

        self.procent = ctk.CTkLabel(self, text="0%")
        self.procent.grid(row=0, column=1)