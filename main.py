from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen


class MyApp(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(
            MDLabel(text="Hello, KivyMD", halign="center")
        )
        return screen


if __name__ == "__main__":
    MyApp().run()
