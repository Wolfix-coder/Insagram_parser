import json
from pathlib import Path

# Шлях до кореневої директорії проекту
PROJECT_ROOT = Path(__file__).parent.parent

from utils.logging import get_logger

# Шляхи до директорій
ASSETS_DIR = PROJECT_ROOT / "assets"
FONT_DIR = ASSETS_DIR / "font"
CONFIG_DIR = PROJECT_ROOT / "config"
LOGS_DIR = PROJECT_ROOT / "logs"
DATA_DIR = PROJECT_ROOT / "data"

# Глобальні налаштування
GUI_SETTINGS = {}
CORE_SETTINGS = {}

logger = get_logger("SETTINGS")

# Налаштування за замовчуванням
DEFAULT_SETTINGS = {
    "theme": "light",
    "font_family": "Inter",
    "font_size": 10,
    "window_width": 900,
    "window_height": 600,
    "language": "uk",
    "auto_save": True,
    "log_level": "INFO"
}


def load_gui_settings():
    """Завантаження налаштувань з JSON файлу"""
    global GUI_SETTINGS
    
    settings_file = CONFIG_DIR / "gui_settings.json"
    
    try:
        if settings_file.exists():
            with open(settings_file, 'r', encoding='utf-8') as f:
                GUI_SETTINGS = json.load(f)
            logger.info(f"Налаштування завантажено з {settings_file}")
        else:
            GUI_SETTINGS = DEFAULT_SETTINGS.copy()
            save_settings()
            logger.info("Створено налаштування за замовчуванням")
    except Exception as e:
        logger.error(f"Помилка завантаження налаштувань: {e}")
        GUI_SETTINGS = DEFAULT_SETTINGS.copy()
    
    return GUI_SETTINGS

def load_core_settings():
    global CORE_SETTINGS
    
    settings_file = CONFIG_DIR / "core_settings.json"
    
    try:
        if settings_file.exists():
            with open(settings_file, 'r', encoding='utf-8') as f:
                CORE_SETTINGS = json.load(f)
            logger.info(f"Налаштування завантажено з {settings_file}")

            return CORE_SETTINGS
        else:
            logger.critical("Помилка при отриманні налаштувань ядра з json", exc_info=True)

            return 0
        
    except Exception:
        logger.critical("Помилка при отриманні налаштувань ядра з json", exc_info=True)


def save_settings():
    """Збереження налаштувань в JSON файл"""
    settings_file = CONFIG_DIR / "gui_settings.json"
    
    try:
        CONFIG_DIR.mkdir(exist_ok=True)
        with open(settings_file, 'w', encoding='utf-8') as f:
            json.dump(GUI_SETTINGS, f, ensure_ascii=False, indent=4)
        print(f"Налаштування збережено в {settings_file}")
        return True
    except Exception as e:
        print(f"Помилка збереження налаштувань: {e}")
        return False


def get_setting(key, default=None):
    """Отримання значення налаштування"""
    return GUI_SETTINGS.get(key, default)


def set_setting(key, value):
    """Встановлення значення налаштування"""
    GUI_SETTINGS[key] = value
    save_settings()