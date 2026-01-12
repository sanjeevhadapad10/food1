import pytest
from food import FoodOrder
def test_total_amount():
    order = FoodOrder(1, "Sanjeev", "Pizza", 2, 300)
    assert order.total_amount() == 600
def test_order_status_premium():
    order = FoodOrder(2, "Rahul", "Burger", 2, 300)
    assert order.order_status() == "Premium Order"
def test_order_status_basic():
    order = FoodOrder(3, "Anita", "Tea", 1, 80)
    assert order.order_status() == "Basic Order"
def test_order_status_invalid():
    order = FoodOrder(4, "Ravi", "Sandwich", 0, 150)
    assert order.order_status() == "Invalid Order"
