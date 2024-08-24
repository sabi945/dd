from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class isi(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'  # Mengatur orientasi BoxLayout menjadi vertikal

        # Buat sebuah BoxLayout untuk menampung button
        bass = BoxLayout(size_hint=(None, None), size=(100, 100))
        bas = Button(text="hallo")
        bass.add_widget(bas)

        # Tambahkan bass (BoxLayout dengan Button di dalamnya) ke dalam layout isi
        self.add_widget(bass)


class Myapp(App):
    def build(self):
        return isi()


if __name__ == "__main__":
    Myapp().run()
