import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

# ========================== Box1 =============================================
class Box1(toga.Box): 

    def __init__(self, on_press, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_press = on_press

        label = toga.Label('This Is Box 1')

        button = toga.Button (
            text="Go To Box2",
            on_press = self.on_press,
            style=Pack(padding=5)
        )

        self.style.update(direction=COLUMN, padding=10)
        self.add(label)
        self.add(button)

