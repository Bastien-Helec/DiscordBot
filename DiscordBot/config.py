# Class Config
class Config:

    # Init
    def __init__(self):
        self.PREFIX = "!"
        self.TOKEN = "NjIyMTI3NzkwMTkxNDExMjEw.G_AA5s.iIXkn7sRI5NVxC_2F2GlWdNjKGQb3whDOJp-Rw"
        self.NAME = "mr.nunusbot#0219"
        self.COLOR = 0xfffffe #la couleur des embeds
        self.VERSION = "2.0.0" #ça on s'en fout mais au cas où
        self.FOOTER = f"© {self.NAME}" #ça c'est ce qu'il y aura écrit en bas des embeds (si tu veux)


# Main
Config = Config()

PREFIX = Config.PREFIX
TOKEN = Config.TOKEN
NAME = Config.NAME
COLOR = Config.COLOR
VERSION = Config.VERSION
FOOTER = Config.FOOTER