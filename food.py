class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_amount(self):
        return self.quantity * self.price

    def order_status(self):
        if self.quantity <= 0:
            return "Invalid Order"

        total = self.total_amount()

        if total >= 500:
            return "Premium Order"
        elif 350 <= total < 500:
            return "Gold Order"
        elif 200 <= total < 350:
            return "Silver Order"
        elif 100 <= total < 200:
            return "Regular Order"
        else:
            return "Basic Order"
