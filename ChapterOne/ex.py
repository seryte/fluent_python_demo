
class Person():
     def __init__(self, name):
          print(f'Initializing the person object...')
          self.name = name
        
     def __new__(cls, num):
          print(f'Creating a new {cls.__name__} object...{num}')
          obj = object.__new__(cls)
          return obj

from dataclasses import dataclass

@dataclass
class InventoryItem:
     """Class for keeping track of an item in inventory."""
     name: str
     unit_price: float
     quantity_on_hand: int = 0

     def total_cost(self) -> float:
          return self.unit_price * self.quantity_on_hand
     def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
          self.name = name
          self.unit_price = unit_price
          self.quantity_on_hand = quantity_on_hand


p1 = InventoryItem(1, 2, 2)
p2 = InventoryItem(1, 2, 2)
print(p1 > p2)
