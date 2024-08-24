from kivy.uix.button import Button
from kivy.app import App
import subprocess

class MyApp(App):
    def build(self):
        # Buat tombol dengan teks "Buka Finder"
        btn = Button(text='Buka Finder', size_hint=(.5, .5), pos_hint={'center_x': .5, 'center_y': .5})
        # Tambahkan aksi untuk membuka Finder ketika tombol ditekan
        btn.bind(on_press=self.buka_finder)
        return btn

    def buka_finder(self, instance):
        # Perintah untuk membuka Finder di macOS
        subprocess.call(["open", "-R", "/"])

if __name__ == "__main__":
    MyApp().run()
