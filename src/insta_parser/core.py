import instaloader

import sys
import json
from pathlib import Path
from itertools import islice
from typing import Any

PARENT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(PARENT_DIR))    # Додавання кореня проекту в імпорти Python

from config.settings import load_core_settings
from utils.logging import get_logger

logger = get_logger("CORE")

class InstaApp:
    def __init__(self):
        self.load_config()
        self.init_loader()
        self.cfg = None

    def load_config(self):
        "Завантажує конфігурації з */src_settings.json"

        self.cfg = load_core_settings()

        self.load_pictures = self.cfg['instaloader']['download_pictures']
        self.load_videos = self.cfg['instaloader']['download_videos']
        self.load_video_thumbnails = self.cfg['instaloader']['download_video_thumbnails']
        self.metadata = self.cfg['instaloader']['save_metadata']
        self.post_metadata = self.cfg['instaloader']['post_metadata_txt_pattern']
        self.quiet_mode = self.cfg['instaloader']['quiet']
        self.san_paths = self.cfg['instaloader']['sanitize_paths']
        self.count = self.cfg['download']['count']
        self.download_path = self.cfg['download']['path']

    def save_to_json(self, path: str, container: str, value: Any):
        """Збереження данних в json файли

            Args:
                path: str -- шлях до json файлу
                container: str -- шлях до комірки з данними які потрібно записати
                value: Any -- значення яке потрібно записати в container
        """

        try:
            with open(path, "r", encoding="UTF-8") as f:
                data = json.load(f)
            
            keys = container.split(".")
            obj = data

            for key in keys[:-1]:
                obj = obj[key]
            obj[keys[-1]] = value

            with open(path, "w", encoding="UTF-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            logger.info(f"Значення ({value}) завантажено в {container}")
            
            return 1
        except Exception as e:
            logger.error(f"Помилка при запису данних в {path}: {e}")
            return 0

    def read_json(self, path: str, container: str) -> Any:
        """Читання данних з json файлу

            Args:
                path: str -- шлях до json файлу
                container: str -- шлях до комірки з данними які потрібно зчитати
            
            Returns:
                any - дані якібули зчитані
        """

        try:
            with open(path, "r", encoding="UTF-8") as f:
                data = json.load(f)
            
            keys = container.split(".")
            value = data

            for key in keys:
                value = value[key]
            return value
        
        except Exception as e:
            logger.error(f"Помилка при читанні данних з {path}: {e}")


    def reload_config(self):
        "Перезавантажує конфігурацію з JSON файлу та переініціалізує Instaloader"
        self.load_config()
        self.init_loader()  # ← ВАЖЛИВО: переініціалізуємо Instaloader з новими параметрами

    def init_loader(self):
        "Створює об'єкт L для доступу до функцій Instaloader за параметрами з */src_settings.json"

        self.L = instaloader.Instaloader(
            download_pictures=self.load_pictures,
            download_videos=self.load_videos,
            download_video_thumbnails=self.load_video_thumbnails,
            save_metadata=self.metadata,
            post_metadata_txt_pattern=self.post_metadata,
            quiet=self.quiet_mode,
            sanitize_paths=self.san_paths
        )

    def download(self, username: str, limit: int, target_dir: str) -> None:
        """Завантажує данні

            Args:
                username: str - юзернейм профілю з якого буде братися інформація
                limit: int - кількість данних яку треба завантажити
                target_dir: str - шлях куди будуть завантажені всі файли
        """

        self.reload_config()

        try:
            profile = instaloader.Profile.from_username(
                self.L.context,
                username
            )

            # target_path = Path(target_dir) / username
            target_path = username
            # target_path.mkdir(parents=True, exist_ok=True)

            for post in islice(profile.get_posts(), limit):
                self.L.download_post(
                    post,
                    target=str(target_path)
                )

            logger.info(
                f"Успішно завантажено {limit} постів користувача {username} "
                f"у папку {target_path}"
            )

        except Exception as e:
            logger.exception(
                f"Помилка при завантаженні контенту користувача {username}: {e}"
            )