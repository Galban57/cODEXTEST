from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar


class MyApp(MDApp):
    """Simple KivyMD application with a counter button."""

    count = 0

    def build(self):
        screen = MDScreen()
        layout = MDBoxLayout(orientation="vertical")

        layout.add_widget(MDTopAppBar(title="Mon app KivyMD"))

        self.label = MDLabel(
            text="Nombre de clics: 0", halign="center"
        )
        layout.add_widget(self.label)

        layout.add_widget(
            MDRaisedButton(
                text="Clique ici",
                pos_hint={"center_x": 0.5},
                on_release=self.increment_count,
            )
        )

        screen.add_widget(layout)
        return screen

    def increment_count(self, *_):
        self.count += 1
        self.label.text = f"Nombre de clics: {self.count}"


if __name__ == "__main__":
    MyApp().run()
