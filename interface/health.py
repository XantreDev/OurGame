from interface.interface_object import InterfaceObject

class HpInterface(InterfaceObject):
    def __init__(self, *args):
        super().__init__(*args)

    def update(self):
        super().update()
        red_deg, green_deg = (100 - self.char.hp) / 100 * 255, (self.char.hp / 100) * 255
        self.color = (red_deg, green_deg, 0)
