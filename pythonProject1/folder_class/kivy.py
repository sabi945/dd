from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operator = ""
        self.last_was_operator = False

        # Membuat tata letak (GridLayout) untuk aplikasi
        layout = GridLayout(cols=4, spacing=10, size_hint=(1, 1.5))
        
        # Membuat widget input teks
        self.text_input = TextInput(multiline=False, readonly=True, halign='right', font_size=32)
        layout.add_widget(self.text_input)

        # Membuat tombol-tombol kalkulator
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for button_text in buttons:
            button = Button(text=button_text, pos_hint={'center_x': 0.5, 'center_y': 0.5})
            button.bind(on_press=self.on_button_press)
            layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        current_text = self.text_input.text
        button_text = instance.text

        if button_text == 'C':
            self.text_input.text = ""
            self.operator = ""
            self.last_was_operator = False
        elif button_text == '=':
            try:
                result = str(eval(current_text))
                self.text_input.text = result
            except Exception as e:
                self.text_input.text = "Error"
        else:
            if self.last_was_operator and button_text in ['+', '-', '*', '/']:
                # Memastikan tidak ada dua operator berturut-turut
                return
            self.text_input.text += button_text
            self.last_was_operator = button_text in ['+', '-', '*', '/']
            if self.last_was_operator:
                self.operator = button_text

if __name__ == '__main__':
    CalculatorApp().run()
