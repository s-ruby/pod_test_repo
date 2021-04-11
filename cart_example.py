class Cart():
    def __init__(self): #attributes
        self.items = []
        
    def add(self, name, price): #add items to our cart
        item = {}
        item['name'] = name #name of item
        item['price'] = price
        self.items.append(item)
        
    def remove(self, itemToRemove):
        for item in self.items: #loops through items list
            if itemToRemove == item['name']: #if item matches item to remove
                self.items.pop(self.items.index(item)) #locates the index of the item to remove and pops it out of list
                return
        print(f'{itemToRemove} not in cart')
        
    def total(self):
        cart_total = 0
        for item in self.items:
            cart_total += item['price']
        return f"${cart_total}"
        
        
myCart = Cart()

myCart.add('bananas', 2)
myCart.add('oreos', 1)

print(myCart.items)

myCart.remove('bananas')
print(myCart.items)

myCart.add('pasta', 1)
print(myCart.total())