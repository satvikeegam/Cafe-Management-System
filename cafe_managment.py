```python
class Restaurant_Management_System:
    def __init__(self, customer_name, customer_mobile_number, table_number,
                 food_items, total_bill, order_status):

        self.customer_name = customer_name
        self.customer_mobile_number = customer_mobile_number
        self.table_number = table_number
        self.food_items = food_items
        self.total_bill = total_bill
        self.order_status = order_status

        self.restaurant_name = "Food Hub"

    def print_details(self):
        print("Customer Name:", self.customer_name)
        print("Customer Mobile Number:", self.customer_mobile_number)
        print("Table Number:", self.table_number)
        print("Food Items:", self.food_items)
        print("Total Bill:", self.total_bill)
        print("Order Status:", self.order_status)
        print("Restaurant Name:", self.restaurant_name)

    def add_food_item(self, food_name, price):
        self.food_items.append(food_name)
        self.total_bill += price
        print(food_name, "added to the order.")
        print("Total Bill:", self.total_bill)

    def check_order_status(self):
        print("Order Status:", self.order_status)

    def update_order_status(self, new_status):
        self.order_status = new_status
        print("Order Status Updated:", self.order_status)

    def update_mobile_number(self, new_mobile_number):
        self.customer_mobile_number = new_mobile_number
        print("Mobile Number Updated:", self.customer_mobile_number)

    def generate_bill(self):
        print("\n----- RESTAURANT BILL -----")
        print("Restaurant Name:", self.restaurant_name)
        print("Customer Name:", self.customer_name)
        print("Table Number:", self.table_number)
        print("Food Items:", self.food_items)
        print("Total Bill: Rs.", self.total_bill)
        print("---------------------------")


customer1 = Restaurant_Management_System(
    "Pranay", "9876543210", 5, ["Burger"], 120, "Order Placed"
)

customer1.print_details()

customer1.add_food_item("Pizza", 200)

customer1.add_food_item("Coffee", 50)

customer1.check_order_status()

customer1.update_order_status("Preparing")

customer1.update_mobile_number("9123456780")

customer1.generate_bill()
```
