import logging
import sys
import os

level = logging.INFO

class GUIHandler(logging.Handler):
    """Handler для виводу логів в GUI textbox"""
    
    _textbox = None  # Спільне для всіх logger'ів
    
    @classmethod
    def set_textbox(cls, textbox):
        cls._textbox = textbox
    
    def emit(self, record):
        if self._textbox is None:
            return
        
        msg = self.format(record)
        # Thread-safe вивід
        self._textbox.after(0, lambda: self._insert(msg))
    
    def _insert(self, msg):
        self._textbox.insert("end", msg + "\n")
        self._textbox.see("end")

def get_logger(name: str = "parser"):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger
    
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(log_format)

    # Консольний обробник (в консоль)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # GUI обробник (в textbox)
    gui_handler = GUIHandler()
    gui_handler.setLevel(level)
    gui_handler.setFormatter(formatter)
    logger.addHandler(gui_handler)

    # Файловий обробник
    log_dir = 'logs/'
    log_path = 'logs/bot.log'
    os.makedirs(log_dir, exist_ok=True)
    file_handler = logging.FileHandler(log_path, encoding='utf-8-sig')
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger