

class Pet:
    def __init__(self, name):
        self.name = name
        self.happy = 100
        self.hunger = 100
        self.health = 100

    def feed(self):
      self.hunger += 20

    def walk(self):
      self.health += 10
      self.happy += 5

    def pet(self):
      self.happy += 10

    def cage(self):
      self.happy -= 10
