import customtkinter as ctk

from utils.logging import get_logger

logger = get_logger("INPUT_FRM")

class InputFrame (ctk.CTkFrame):

    def __init__(self, master, core, parent_dir):
        super().__init__(master, fg_color="transparent")

        self.core = core

        self.PARENT_DIR = parent_dir

        self.label = ctk.CTkLabel(self, text="Input")
        self.label.grid(row=0, column=0, sticky="w", padx=10)

        self.entry = ctk.CTkEntry(self, placeholder_text="Instagram username", width=360)
        self.entry.grid(row=0, column=1, sticky="ew", padx=(50, 30))

        self.fetch_btn = ctk.CTkButton(self, text="Fetch Data", width=85, command=self.selected_username)
        self.fetch_btn.grid(row=0, column=2)

        # self.grid_columnconfigure(0, weight=1)

    def selected_username(self):
        "Зберігає username в json"

        try:
            path = self.PARENT_DIR / "config" / "core_settings.json"
            container = "download.username"
            value = str(self.entry.get())

            self.core.save_to_json(path, container, value)
        except Exception as e:
            logger.error(f"Помилка при передаванні данних з InputFrame() до core.save_to_json: {e}")