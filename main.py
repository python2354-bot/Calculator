from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

import ast
import operator as op

# Simple, safe evaluator for + - * / and power, parentheses, floats
_ALLOWED = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}

def _eval_node(node):
    if isinstance(node, ast.Num):  # <number>
        return node.n
    if isinstance(node, ast.UnaryOp) and type(node.op) in (ast.UAdd, ast.USub):
        return _ALLOWED[type(node.op)](_eval_node(node.operand))
    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED:
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        return _ALLOWED[type(node.op)](left, right)
    if isinstance(node, ast.Expr):
        return _eval_node(node.value)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'round' and len(node.args) in (1, 2):
        args = [_eval_node(a) for a in node.args]
        return round(*args)
    if isinstance(node, ast.Module):
        # Python >=3.8 uses ast.Module(body=[...], type_ignores=[])
        if node.body:
            return _eval_node(node.body[0])
    raise ValueError("Invalid expression")

def safe_eval(expr):
    try:
        tree = ast.parse(expr, mode='exec')
        return _eval_node(tree)
    except Exception as e:
        raise ValueError(str(e))

class Display(Label):
    pass

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.display = Display(text="0", font_size='48sp', size_hint=(1, 0.25), halign='right', valign='middle')
        self.display.bind(size=self._update_text)
        self.add_widget(self.display)

        grid = GridLayout(cols=4, spacing=4, padding=4)
        buttons = [
            ('C', self.clear), ('⌫', self.backspace), ('(', self.add_char), (')', self.add_char),
            ('7', self.add_char), ('8', self.add_char), ('9', self.add_char), ('/', self.add_char),
            ('4', self.add_char), ('5', self.add_char), ('6', self.add_char), ('*', self.add_char),
            ('1', self.add_char), ('2', self.add_char), ('3', self.add_char), ('-', self.add_char),
            ('0', self.add_char), ('.', self.add_char), ('^', self.add_pow), ('+', self.add_char),
            ('=', self.calculate),
        ]

        for text, handler in buttons:
            btn = Button(text=text, font_size='24sp')
            btn.bind(on_press=handler)
            # make "=" span 4 columns width visually by increasing size_hint_y if last row? we'll keep simple
            grid.add_widget(btn)

        self.add_widget(grid)

    def _update_text(self, *_):
        self.display.text_size = (self.display.width - 20, None)

    def add_char(self, instance):
        ch = instance.text
        if self.display.text == "0" and ch not in ('.', ')'):
            self.display.text = ch
        else:
            self.display.text += ch

    def add_pow(self, instance):
        # map '^' to '**'
        if self.display.text == "0":
            self.display.text = ""
        self.display.text += '**'

    def clear(self, *_):
        self.display.text = "0"

    def backspace(self, *_):
        t = self.display.text
        if t.endswith('**'):
            t = t[:-2]
        elif t != "0":
            t = t[:-1]
        if not t:
            t = "0"
        self.display.text = t

    def calculate(self, *_):
        expr = self.display.text
        try:
            result = safe_eval(expr)
            # format nicely: int if whole, else rounded
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            else:
                # keep reasonable precision
                result = round(result, 10)
            self.display.text = str(result)
        except Exception:
            self.display.text = "Error"

class CalcApp(App):
    def build(self):
        self.title = "CalcApp"
        Window.minimum_width, Window.minimum_height = 360, 640
        return Calculator()

if __name__ == "__main__":
    CalcApp().run()