import customtkinter as ctk

from utils.logging import get_logger

logger = get_logger("RAD_WIDGET")

class RadioButWidget(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.selected_value = ctk.IntVar(value=1)

        self.radiobutton_5 = ctk.CTkRadioButton(self, text="  5", variable=self.selected_value, value=5, command=self.update_entry_state)
        self.radiobutton_5.grid(row=0, column=0, padx=10, pady=10)

        self.radiobutton_10 = ctk.CTkRadioButton(self, text="  10", variable=self.selected_value, value=10, command=self.update_entry_state)
        self.radiobutton_10.grid(row=1, column=0, padx=10, pady=10)

        self.radiobutton_20 = ctk.CTkRadioButton(self, text="  20", variable=self.selected_value, value=20, command=self.update_entry_state)
        self.radiobutton_20.grid(row=0, column=1, pady=10)

        self.radiobutton_custom = ctk.CTkRadioButton(self, text="", variable=self.selected_value, value=50, command=self.update_entry_state)
        self.radiobutton_custom.grid(row=1, column=1, pady=10)

        self.entry = ctk.CTkEntry(self, width=50, placeholder_text="50", state="disabled")
        self.entry.grid(row=1, column=1, padx=(20, 0), pady=10)

    def update_entry_state(self):
        """Активує або деактивує поле четвертої кнопки"""
        try:
            if self.selected_value.get() == 50:  # якщо вибрана четверта кнопка
                self.entry.configure(state="normal")
            else:
                self.entry.delete(0, "end")  # очистка поля при перемиканні
                self.entry.configure(state="disabled")

        except Exception as e:
            logger.debug(f"selected_value = {self.selected_value}")
            logger.error(f"Помилка при роботі з полем: {e}")

    def get_value(self):
        """
        Повертає кінцеве значення:
        - якщо обрана custom-кнопка — бере з entry
        - інакше — бере з selected_value
        """
        try:
            if self.selected_value.get() == 50:
                value = self.entry.get()

                if not value.isdigit():
                        raise ValueError("Custom value is not a number")
                return int(value)

            return self.selected_value.get()
        except Exception as e:
            logger.error(f"Помилка при отриманні отриманні значення з option radiobutton: {e}")