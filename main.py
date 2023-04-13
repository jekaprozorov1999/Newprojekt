from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class jekaApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, mrjeka", halign="center")


jekaApp().run()