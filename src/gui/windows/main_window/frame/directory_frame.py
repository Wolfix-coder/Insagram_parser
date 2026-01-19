import customtkinter as ctk
from customtkinter import filedialog

class DirectoryFrame (ctk.CTkFrame):

    def __init__(self, master, core, PARENT_DIR):
        super().__init__(master, fg_color="transparent")

        self.core = core
        self.PARENT_DIR = PARENT_DIR

        self.label = ctk.CTkLabel(self, text="Directory")
        self.label.grid(row=0, column=0, sticky="w", padx=10)

        self.entry = ctk.CTkEntry(self, placeholder_text="C:/output", width=360)
        self.entry.grid(row=0, column=1, sticky="ew", padx=(28, 30))

        self.directory_btn = ctk.CTkButton(self, text="Browse", width=85, command=self.selected_path)
        self.directory_btn.grid(row=0, column=2)

        # self.grid_columnconfigure(0, weight=1)

    def selected_path(self):

        folder = filedialog.askdirectory(title="Виберіть папку")

        if folder:
            self.entry.delete(0, "end")
            self.entry.insert(0, folder)
            
            path = self.PARENT_DIR / "config" / "core_settings.json"
            container = "download.path"

            self.core.save_to_json(path, container, folder)



