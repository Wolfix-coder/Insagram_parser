import sys
import os
from pathlib import Path

# Додаємо кореневу директорію проекту до шляху
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Імпорти стандартних бібліотек
from datetime import datetime

# Імпорт CustomTkinter
try:
    import customtkinter as ctk
except ImportError:
    print("Помилка: customtkinter не встановлено!")
    print("Встановіть: pip install customtkinter")
    sys.exit(1)

# Імпорти з вашого проекту - ВИПРАВЛЕНІ ПІД ВАШУ СТРУКТУРУ
try:
    # Ваш готовий logger (у вас є utils/logging.py)
    from utils.logging import get_logger
    
    # Ваше готове головне вікно (у вас є src/main_window.py)
    from src.gui.main_window import MainWindow

    # Імпорт ядра
    from src.insta_parser.core import InstaApp
    
    # Налаштування (у вас є config/settings.py)
    from config.settings import load_settings, save_settings, SETTINGS
    
    # Допоміжні функції (у вас є utils/main.py)
    # from utils.main import ensure_directories  # якщо є така функція
    
except ImportError as e:
    print(f"Помилка імпорту: {e}")
    print("Перевірте структуру проекту та назви модулів")
    print(f"\nПоточна директорія: {os.getcwd()}")
    print(f"PROJECT_ROOT: {PROJECT_ROOT}")
    import traceback
    traceback.print_exc()
    sys.exit(1)


def ensure_directories():
    """Створення необхідних директорій"""
    directories = [
        PROJECT_ROOT / "logs",
        PROJECT_ROOT / "data" / "input",
        PROJECT_ROOT / "data" / "output",
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


def initialize_logger():
    """Ініціалізація системи логування"""
    try:
        # Використовуємо ваш готовий logger
        logger = get_logger("MAIN")
        logger.info("=" * 70)
        logger.info("PARSER - Запуск програми")
        logger.info(f"Час запуску: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info(f"Python версія: {sys.version}")
        logger.info(f"Робоча директорія: {PROJECT_ROOT}")
        logger.info("=" * 70)
        return logger
    except Exception as e:
        print(f"Помилка ініціалізації logger: {e}")
        import traceback
        traceback.print_exc()
        # Створюємо базовий logger як fallback
        import logging
        logging.basicConfig(level=logging.INFO)
        return logging.getLogger(__name__)


def check_environment():
    """Перевірка робочого середовища"""
    logger = get_logger()
    
    # Перевірка версії Python
    if sys.version_info < (3, 7):
        logger.error("Потрібна версія Python 3.7 або вище!")
        return False
    
    # Перевірка CustomTkinter
    try:
        ctk_version = ctk.__version__
        logger.info(f"CustomTkinter версія: {ctk_version}")
    except:
        logger.warning("Не вдалося визначити версію CustomTkinter")
    
    return True


def setup_customtkinter():
    """Налаштування CustomTkinter"""
    logger = get_logger()
    
    try:
        # Завантаження налаштувань
        load_settings()
        
        # Налаштування теми з settings або за замовчуванням
        theme = SETTINGS.get('theme', 'dark')
        color_theme = SETTINGS.get('color_theme', 'blue')
        
        ctk.set_appearance_mode(theme)  # "dark", "light", "system"
        ctk.set_default_color_theme(color_theme)  # "blue", "green", "dark-blue"
        
        logger.info(f"CustomTkinter налаштовано: theme={theme}, color={color_theme}")
        
    except Exception as e:
        logger.warning(f"Помилка налаштування CustomTkinter: {e}")
        logger.info("Використовуються стандартні налаштування")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")


def main():
    """Головна функція запуску програми"""
    
    # Ініціалізація logger
    logger = initialize_logger()
    
    try:
        # Перевірка середовища
        logger.info("Перевірка робочого середовища...")
        if not check_environment():
            logger.error("Перевірка середовища не пройдена")
            return 1
        
        # Створення необхідних директорій
        logger.info("Перевірка директорій...")
        ensure_directories()
        
        # Налаштування CustomTkinter
        logger.info("Налаштування CustomTkinter...")
        setup_customtkinter()
        
        # Створення головного вікна
        logger.info("Створення головного вікна...")
        gui = MainWindow()  # Ваш клас головного вікна
        
        logger.info("GUI створено успішно")
        logger.info("Програма готова до роботи")
        logger.info("-" * 70)
        
        # Запуск головного циклу
        logger.info("Запуск головного циклу програми...")
        gui.mainloop()
        
        # Після закриття вікна
        logger.info("-" * 70)
        logger.info("Головний цикл завершено")
        
        # Збереження налаштувань при виході
        logger.info("Збереження налаштувань...")
        save_settings()
        
        logger.info("Програма завершена успішно")
        logger.info("=" * 70)
        return 0
        
    except KeyboardInterrupt:
        logger.info("\nПрограму перервано користувачем (Ctrl+C)")
        return 130
        
    except Exception as e:
        logger.exception(f"Критична помилка: {e}")
        logger.error("=" * 70)
        
        # Показати повідомлення про помилку (якщо можливо)
        try:
            import tkinter.messagebox as messagebox
            messagebox.showerror(
                "Критична помилка", 
                f"Виникла критична помилка:\n\n{str(e)}\n\n"
                f"Деталі в логах: {PROJECT_ROOT / 'logs'}"
            )
        except:
            pass
        
        return 1
    
    finally:
        logger.info("Завершення роботи програми")


if __name__ == "__main__":
    # Запуск програми
    exit_code = main()
    sys.exit(exit_code)