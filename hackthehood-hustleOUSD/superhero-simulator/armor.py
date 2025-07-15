import random

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = int(max_block)

    def block(self):
        blocked = random.randint(0, self.max_block)  
        return blocked

if __name__ == "__main__":
    shield = Armor("Shield", 100)
    print(shield.block())