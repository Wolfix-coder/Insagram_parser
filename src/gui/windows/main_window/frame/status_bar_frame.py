import customtkinter as ctk

from src.gui.windows.main_window.widgets.status_bar_widget import StatusWidget

from utils.logging import get_logger

logger = get_logger("STAT_BAR_FRM")

class StatusBarFrame(ctk.CTkFrame):
    def __init__ (self, master, core, PARENT_DIR):
        super().__init__(master, fg_color="transparent")

        self.core = core
        self.PARENT_DIR = PARENT_DIR

        self.label = ctk.CTkLabel(self, text="Status")
        self.label.grid(row=0, column=0, padx=10)

        StatusWidget(self).grid(row=0, column=1, sticky="ew")

        self.start_btn = ctk.CTkButton(self, text="Start", width=85, command=self.start_download)
        self.start_btn.grid(row=0, column=2, padx=20)

    def start_download(self):
        try:
            json_path = self.PARENT_DIR / "config" / "core_settings.json"
            
            username_container = "download.username"
            count_container = "download.count"
            download_path_container = "download.path"

            username = self.core.read_json(json_path, username_container)
            count = self.core.read_json(json_path, count_container)
            download_path = self.core.read_json(json_path, download_path_container)


            self.core.download(username=username,
                               limit=count,
                               target_dir=download_path)


        except Exception as e:
            logger.error(f"Помилка при передаванні данних до ядра {e}")
