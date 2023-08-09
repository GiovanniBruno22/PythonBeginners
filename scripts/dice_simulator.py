import random

class DiceSimulator:
    def __init__(self, dices: int, dice_faces: int) -> None:
        self.dices = dices
        self.dice_faces = dice_faces
    
    def __str__(self) -> str:
        return f"Dices: {self.dices} Number of faces: {self.dice_faces}"
    
    def get_dices(self) -> int:
        return self.dices
    
    def get_faces(self) -> int:
        return self.dice_faces
    
    def roll(self) -> list:
        total_rolls = []
        
        for _ in range(self.dices):
            total_rolls.append(random.randint(1, self.dice_faces))

        return total_rolls
    

if __name__ == "__main__":
    dice = DiceSimulator(2, 6)
    print(dice)

    total = dice.roll()
    print(f"{total} total: {sum(total)}")

