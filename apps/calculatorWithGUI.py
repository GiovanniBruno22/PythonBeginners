from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = None
        self.last_button = None
        self.result = TextInput(
            multiline=False, readonly=True, halign='right', font_size=100
        )
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.result)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '%', '+'],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                )
                if label == '%':
                    button.bind(on_press=self.on_mod)
                elif label == 'C':
                    button.bind(on_press=self.on_clear)
                else:
                    button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        # Add a Mod button
        equals_button = Button(
            text='=', pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        layout.add_widget(equals_button)

        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if current == 'Error':
            self.result.text = ''

        new_text = current + button_text
        self.result.text = new_text

    def on_solution(self, instance):
        text = self.result.text
        try:
            answer = str(eval(self.result.text))
            self.result.text = answer
        except Exception:
            self.result.text = 'Error'

    def on_clear(self, instance):
        self.result.text = ''

    def on_mod(self, instance):
        current = self.result.text
        if current == 'Error':
            self.result.text = ''
        new_text = current + '%'
        self.result.text = new_text


if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
