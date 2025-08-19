from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.display = TextInput(
            text="", readonly=True, halign="right",
            font_size=48, size_hint=(1, 0.25)
        )
        self.add_widget(self.display)

        grid = GridLayout(cols=4)
        for text in ["7","8","9","/",
                     "4","5","6","*",
                     "1","2","3","-",
                     "0",".","=","+"]:
            btn = Button(text=text, font_size=32)
            btn.bind(on_press=self.on_press)
            grid.add_widget(btn)
        self.add_widget(grid)

    def on_press(self, btn):
        ch = btn.text
        if ch == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except Exception:
                self.display.text = "Ошибка"
        else:
            self.display.text += ch

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == "__main__":
    CalculatorApp().run()
