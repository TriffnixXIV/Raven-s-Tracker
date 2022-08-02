import tkinter as tk
from tkinter import ttk

class Tabs(tk.Frame):
    class TabLabel(tk.Label):

        def __init__(self, index, tabs, **kwargs):
            super().__init__(tabs.top_frame, **kwargs)
            self.tabs = tabs
            self.index = index
            self.bind("<Button-1>", self.on_click)
        
        def on_click(self, *_):
            self.tabs.set_tab(self.index)

    def __init__(self,
    parent,
    active_configure: dict[str]={},
    inactive_configure: dict[str]={},
    content_grid_options: dict[str]={},
    **kwargs):
        super().__init__(parent, **kwargs)

        self.index: int = -1
        self.tab_count: int = 0

        self.labels: list[tk.Label] = []
        self.widgets: list[tk.Widget] = []

        self.active_configure = active_configure
        self.inactive_configure = inactive_configure
        self.content_grid_options = content_grid_options

        bg = self.cget("bg")

        self.top_frame = tk.Frame(self, bg=bg)
        self.top_frame.grid(row=0, column=0, padx=0, pady=0, sticky="we")
        ttk.Separator(self, orient="horizontal").grid(row=1, sticky="we")

    def set_active_configure(self, **kwargs):
        self.active_configure = kwargs
        if self.index != -1:
            self.labels[self.index].configure(**kwargs)
    
    def set_inactive_configure(self, **kwargs):
        self.inactive_configure = kwargs
        for index, label in enumerate(self.labels):
            if index != self.index:
                label.configure(**kwargs)
    
    def set_grid_options(self, **kwargs):
        self.grid_options = kwargs
        self.set_tab(self.index)

    def add_tab(self, title: str, widget: tk.Widget):
        label = self.TabLabel(self.tab_count, self, **self.inactive_configure, text=title)
        label.grid(row=0, column=self.tab_count, padx=0, sticky="nswe")

        self.widgets.append(widget)
        self.labels.append(label)
        self.tab_count += 1

        if self.tab_count == 1:
            self.set_tab(0)

    def set_tab(self, index: int):
        self.widgets[self.index].grid_forget()
        self.labels[self.index].configure(**self.inactive_configure)
        self.index = index
        self.widgets[self.index].grid(row=2, column=0, **self.content_grid_options)
        self.labels[self.index].configure(**self.active_configure)

def main():
    root = tk.Tk()
    bg0 = "#101010"
    bg1 = "#303030"
    fg = "#F6F6F6"

    tabs = Tabs(root, bg=bg0)
    tabs.grid(row=0, column=0)

    tabs.set_active_configure(bg=bg1, fg=fg, font=("Helvetica", 10))
    tabs.set_inactive_configure(bg=bg0, fg=fg, font=("Helvetica", 8))

    for i in range(10):
        tabs.add_tab(f"Tab {i}", tk.Label(tabs, text=f"Content {i}", bg=bg1, fg=fg))
    
    root.mainloop()

if __name__ == "__main__":
    main()