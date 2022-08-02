class WidgetColours:
    
    def __init__(self,bg0="#E0E0E0",bg1="#F6F6F6",fg="#000000",sc="#F6FFF6"):
        self.bg0 = bg0
        self.bg1 = bg1
        self.fg = fg
        self.sc = sc
        self.f = {"bg": bg1}
        self.f0 = {"bg": bg0}
        self.c = {"bg": bg1}
        self.c0 = {"bg": bg0}
        self.b = {"activebackground": bg0, "activeforeground": fg,
                  "bg": bg1, "fg": fg}
        self.l = {"bg": bg1, "fg": fg}
        self.l0 = {"bg": bg0, "fg": fg}
        self.cb = {"selectcolor": bg0,
                   "activebackground": bg0, "activeforeground": fg,
                   "bg": bg1, "fg": fg}
        self.e = {"bg": bg1, "fg": fg}
        self.e0 = {"bg": bg0, "fg": fg}
        self.io = {"activebackground": bg0, "highlightcolor": sc,
                   "bg": bg1, "fg": fg}
        self.sb = {"activebackground": bg1,
                   "bg": bg0,
                   "troughcolor": bg1}

dark = WidgetColours("#101010","#202020","#E0E0E0","#204020")