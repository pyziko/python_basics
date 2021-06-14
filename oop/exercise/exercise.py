class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        self.items.append({"name": name, "price": price})

    def stock_price(self):
        total = 0
        return sum(list(x['price'] for x in self.items))
        # for dic in self.items:
        #     price = dic['price']
        #     total += price
        # return total
# Add together all item prices in self.items and return the total.

