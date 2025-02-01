class Purchase:
    
    purchase_count = 0 # Static attribute

    def __init__(self, product:str, price:float, quantity:int):
        self.product = product
        self.quantity = quantity
        self.price = price
        Purchase.purchase_count += 1

    def total(self):
        return self.price * self.quantity


purchase1 = Purchase("Monitor", 45000, 2)
print(f"Product:{purchase1.product}, Quantity:{purchase1.quantity}")
print(f"Total:{purchase1.total()}")