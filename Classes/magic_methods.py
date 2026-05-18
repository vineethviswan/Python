
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item} not in the cart.")

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return f"Cart with {len(self)} items: {', '.join(self.items)}"

    def __getitem__(self, index):
        return self.items[index]

    def __iter__(self):
        return iter(self.items)

    def list_items(self):
        return self.items

cart = Cart()
cart.add_item('Laptop')
cart.add_item('Wireless mouse')
cart.add_item('Ergo keyboard')
cart.add_item('Monitor')

for item in cart:
    print(item, end=' ')

print(len(cart))  # Output: 4
print(cart[2])  # Output: Ergo keyboard

print('Monitor' in cart) # True
print('banana' in cart) # False

cart.remove_item('Ergo keyboard')

print(cart.list_items()) # ['Laptop', 'Wireless mouse', 'Monitor']

cart.remove_item('banana') # banana is not in cart