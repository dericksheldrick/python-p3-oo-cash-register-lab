#!/usr/bin/env python3

#pseudocode
# define a class called CashRegister
# pass quanties and prices as a parameter
# create quantity  method and its attributes should be protected 
# create a apply_discount method that calculate the discount thy get
# calculate price after discount (price - discount)
# keep track of what has been added by adding the amount of quantities added
# create void_last_transcantion that clear tha last transcantion

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = []
  
  
  def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.last_transaction.append(
            {"item": item, "quantity": quantity, "price": price}
        )
    
  
  def apply_discount(self):
    if self.discount:
        self.total = int(self.total * ((100 - self.discount) / 100))
        print(f"After the discount, the total comes to ${self.total}.")
    else:
        print("There is no discount to apply.")

  def void_last_transaction(self):
    if not self.last_transaction:
            return "There are no transactions to void."
    self.total -= (
            self.last_transaction[-1]["price"]
            * self.last_transaction[-1]["quantity"]
    )
    for _ in range(self.last_transaction[-1]["quantity"]):
            self.items.pop()
    self.last_transaction.pop()




stock = CashRegister(20)
stock.add_item("egg", 60, 3)
print(stock.apply_discount())
