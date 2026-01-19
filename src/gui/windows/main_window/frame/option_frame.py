import customtkinter as ctk

class OptionFrame (ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        self.option_btn = ctk.CTkButton(self, text="Option", width=500, command=self.open_options)
        self.option_btn.grid(row=0, column=0, padx=40)

    def open_options(self):
        """Коли натиснули кнопку - шукаємо App і викликаємо його функцію"""
        # Піднімаємося по ієрархії вгору до App
        widget = self
        while widget.master:
            widget = widget.master
            # Коли знайшли App - викликаємо його open_options()
            if widget.__class__.__name__ == 'App':
                widget.open_options()  # це викличе функцію з app.py
                return
