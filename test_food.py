from food import FoodOrder
def test_total_amount():
    print(">>> Running test_total_amount")
    order = FoodOrder(1, "Sanjeev", "Pizza", 2, 300)
    print("Total Amount =", order.total_amount())
    assert order.total_amount() == 600
def test_order_status_premium():
    print(">>> Running test_order_status_premium")
    order = FoodOrder(2, "Rahul", "Burger", 2, 300)
    print("Order Status =", order.order_status())
    assert order.order_status() == "Premium Order"
def test_order_status_basic():
    print(">>> Running test_order_status_basic")
    order = FoodOrder(3, "Anita", "Tea", 1, 80)
    print("Order Status =", order.order_status())
    assert order.order_status() == "Basic Order"
def test_order_status_invalid():
    print(">>> Running test_order_status_invalid")
    order = FoodOrder(4, "Ravi", "Sandwich", 0, 150)
    print("Order Status =", order.order_status())
    assert order.order_status() == "Invalid Order"
