import customtkinter as ctk

from utils.logging import get_logger

logger = get_logger("OPT.BTN_FRAME")

class ButtonFrame(ctk.CTkFrame):
    def __init__(self, master, core, PARENT_DIR, downloads_frame):
        super().__init__(master, fg_color="transparent")

        self.core = core
        self.PARENT_DIR = PARENT_DIR
        self.downloads_frame = downloads_frame

        self.save_button = ctk.CTkButton(self, width=150, text="Save", command=self.save_settings)
        self.save_button.grid(row=0, column=0, sticky="ew")

    def save_settings(self):
        """Зберігає налаштування при натисканні кнопки"""
        try:

            path = self.PARENT_DIR / "config" / "core_settings.json"
            container = "download.count"

            # Отримуємо АКТУАЛЬНЕ значення при натисканні кнопки
            value = self.downloads_frame.radio_but_widget.get_value()

            # Зберігаємо
            result = self.core.save_to_json(path, container, value)

            if result:
                logger.info(f"Налаштування збережено: {value}")
            else:
                logger.error("Не вдалось зберегти налаштування")
                
        except Exception as e:
            logger.error(f"Помилка збереження: {e}")
            logger.info(value)

