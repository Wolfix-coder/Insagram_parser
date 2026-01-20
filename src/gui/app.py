import customtkinter as ctk

from src.insta_parser.core import InstaApp

from .windows.main_window.window.main_window import MainWindow
from .windows.option_window.window.option_window import OptionWindow

class App (ctk.CTk):
    def __init__ (self, PARENT_DIR: str):
        super().__init__()

        self.core = InstaApp()
        self.PARENT_DIR = PARENT_DIR

        self.title("Instagram Parser v1.0")
        self.geometry("600x400")

        self.main_window = MainWindow(self)
        self.main_window.pack(fill="both", expand=True)

    def open_options(self):
        """Ця функція відкриває вікно налаштувань"""
        option_window = OptionWindow(
            self,  # передаємо App як батьківське вікно
            core=self.core,  # передаємо core
            parent_dir=self.PARENT_DIR  # передаємо директорію
        )