from __future__ import annotations
from typing import Optional

class Basket:
    eggs: list[str]

    def __init__(self, starting: Optional(list[str]) = []) -> None:
        if len(starting) > 0:
            self.eggs = starting
        else:
            self.eggs = []

    def is_full(self) -> bool:
        if len(self.eggs) >= 5:
            return True
        return False

    def same_color(self, other: Basket) -> bool:
        for egg_1 in self.eggs:
            for egg_2 in other.eggs: 
                if egg_1 == egg_2:
                    return True
        return False


b1: Basket = Basket(["blue", "yellow"])
b2: Basket = Basket()
b3: Basket = Basket(["orange", "red", "green", "blue", "white"])

print(b3.is_full())
print(b1.same_color(b3))