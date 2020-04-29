class Weapon:
    def __init__(self, speeding = 20, Worker = None, Character = None):
        self.worker = Worker
        self.character = Character
        self.speeding = speeding
        self.status = False
        self.timer = 0
    
    def activate(self):
        self.status = True
    
    def run(self):
        pass
    
    def deactivate(self):
        self.status = False