class Cart():
    def __init__(self):
        self.items = []
  
    def add(self, name, price):
        item = {}
        item['name'] = name
        item['price'] = price
        self.items.append(item)
        
        
    def remove(self, itemToRemove):
        for item in self.items:
            if itemToRemove == item['name']:
                self.items.pop(self.items.index(item))
                return
        print(f'{itemToRemove} not in cart')
    
instaCart = Cart()

# add a few items
instaCart.add('oreos', 12)
instaCart.add('bananas', 2)
instaCart.remove('oreos')

print(instaCart.items) # [{'name': 'oreos', 'price': 12}, {'name': 'bananas', 'price': 2}]

instaCart.add('rice', 5)
instaCart.remove('cookies')