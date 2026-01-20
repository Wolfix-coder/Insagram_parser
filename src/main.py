import sys
import os
from pathlib import Path
from datetime import datetime

# --- Не міняти місцями з імпортами пакетів --- CRITICAL
PARENT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(PARENT_DIR))    # Додавання кореня проекту в імпорти Python


from src.insta_parser.core import InstaApp
from src.gui.app import App
from config.settings import load_gui_settings, load_core_settings
from utils.logging import get_logger


logger = get_logger('MAIN')     # Створення логера

class Setup:

    def __init__(self, core, gui) -> None:
        self.core = core
        self.gui = gui

    def load_json_settings(self):
        "Завантаження параметрів проекту"

        try:
            self.gui_settings = load_gui_settings()

            logger.info("Параметри GUI завантажені УСПІШНО")
            logger.info("Використовуються наступні параметри GUI програми")
            print("\n", self.gui_settings, "\n")

        except Exception:
            logger.critical(f"Конфігурації вікна не були завантажені: \n", exc_info=True)

        try:
            self.core_settings = load_core_settings()

            logger.info("Параметри CORE завантажено УСПІШНО")
            logger.info("Використовуються наступні параметри CORE програми")
            print("\n", self.core_settings, "\n")

        except Exception:
            logger.critical(f"Конфігурації вікна не були завантажені: \n", exc_info=True)

    def init_core(self):
        "Ініціалізація ядра"

        try:
            logger.info("Ініціалізація головного ядра програми")
            # core = InstaApp()

            self.core.reload_config()

            logger.info("Ініціалізація головного ядра програми завершилася УСПІШНО")
        except Exception:
            logger.critical(f"Ядро не було завантажене: \n", exc_info=True)

        
    def init_gui(self):
        "Ініціалізація ядра"

        try:
            logger.info("Ініціалізація головного вікна програми")

            self.gui()

            logger.info("Ініціалізація головного вікна програми завершилася УСПІШНО")
        except Exception:
            logger.critical(f"Головне вікно не було завантажене: \n", exc_info=True)


    def main(self):
        try:
            logger.info("PARSER - Запуск програми")
            logger.info(f"Час запуску: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            logger.info(f"Python версія: {sys.version}")
            logger.info(f"Робоча директорія: {PARENT_DIR}")
            logger.info("=" * 70)

            self.load_json_settings()

            logger.info("=" * 70)

            self.init_core()

        except Exception:
            logger.critical("Фатальна помилка при запуску програми", exc_info=True)
    

if __name__ == "__main__":
    core = InstaApp()

    gui = App(PARENT_DIR)

    setup = Setup(core, gui)
    setup.main()

    gui.mainloop()

