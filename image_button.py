import tkinter as tk

class ImageButton(tk.Label):

    def __init__(self, parent, inactive_image, active_image, command, **kwargs):
        self.inactive_image = inactive_image
        self.active_image = active_image
        super().__init__(parent, image=inactive_image, highlightthickness=0, borderwidth=0, **kwargs)

        self.bind("<Button-1>", lambda x: command(x))
        self.bind("<Enter>", lambda *_: self.activate())
        self.bind("<Leave>", lambda *_: self.deactivate())

    def activate(self):
        self.configure(image=self.active_image)
    
    def deactivate(self):
        self.configure(image=self.inactive_image)