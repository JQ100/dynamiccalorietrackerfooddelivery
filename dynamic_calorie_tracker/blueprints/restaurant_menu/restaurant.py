class Restaurant:
    def __init__(self):
        self.name = ""
        self.menu_items = {}
        self.customer_orders = []

    def add_item_to_menu(self, num_id=int, item=str, price=float, calories=int):
        self.menu_items[item] = (num_id, price, calories)

    def customer_order(self, order_id, order_list):
        order_details = {'Order ID': order_id, 'order': order_list}
        self.customer_orders.append(order_details)

    def print_menu_items(self):
        for item, info in self.menu_items.items():
            print("{}: {}".format(item, (info)))

    def print_customer_orders(self):
        for order in self.customer_orders:
            print("Order No. {}: {}".format(order['Order ID'], order['order']))

    def get_calories(self, item):
        return ""
    
restaurant = Restaurant()

# Add items
restaurant.add_item_to_menu(0, "Cheeseburger", 4, 300)
restaurant.add_item_to_menu(1,"Hamburger", 3, 250)
restaurant.add_item_to_menu(2,"Double Krabby Patty", 5.50, 500)
restaurant.add_item_to_menu(3,"Double Krabby Patty with Cheese", 7.50, 450)
restaurant.add_item_to_menu(4,"French Fries Plate", 5, 480)
restaurant.add_item_to_menu(5,"Wild Pollock Fish & Chips:", 15, 710)
restaurant.add_item_to_menu(6,"Coleslaw", 2.50, 290)
restaurant.add_item_to_menu(7,"10 pc Chicken Nuggets", 8, 520)
restaurant.add_item_to_menu(8,"5 pc Chicken Tenders", 7, 740)
restaurant.add_item_to_menu(9,"5 pc Chicken Wings", 5, 700)
restaurant.add_item_to_menu(10,"Filet O Fish", 2.50, 390)

# Order items
restaurant.customer_order(5, ["Cheeseburger", "Filet O Fish", "Coleslaw"])
restaurant.customer_order(6, "Grilled Salmon")
restaurant.customer_order(77, "Fish & Chips")
restaurant.customer_order(4, "Grilled Salmon")

print("\nPopular dishes in the restaurant along with their prices:")
restaurant.print_menu_items()

print("\nPrint customer orders:")
restaurant.print_customer_orders()

restaurant1 = Restaurant()

restaurant1.add_item_to_menu(11, "Chicken and Corn Rice Bowl", 8, 645)
restaurant1.add_item_to_menu(12, "Greek Salad", 9, 600)
restaurant1.add_item_to_menu(13, "Caesar Salad", 5.50, 550)
restaurant1.add_item_to_menu(14, "Rotisserie Chicken Salad", 7.50, 710)
restaurant1.add_item_to_menu(15, "Crispy Falafel Wrap", 8.50, 955)
restaurant1.add_item_to_menu(16, "Pita Wrap", 6, 540)
restaurant1.add_item_to_menu(17, "Pita Chips", 2, 280)
restaurant1.add_item_to_menu(18, "Side Hummus", 1, 135)

# Order items
restaurant1.customer_order(2,["Greek Salad", "Pita Wrap"])
restaurant1.customer_order(23, "Pita Chips")
restaurant1.customer_order(45, "Side Hummus")
restaurant1.customer_order(63, "Crispy Falafel Wrap")

print("\nPopular dishes in the restaurant along with their prices:")
restaurant1.print_menu_items()

print("\nPrint customer orders:")
restaurant1.print_customer_orders()

restaurant2 = Restaurant()
restaurant2.add_item_to_menu(20, "Cinnamon Roll", 3.50, 880)
restaurant2.add_item_to_menu(21, "Twisted Churro", 1.50, 570)
restaurant2.add_item_to_menu(22, "Chocolate Chip Cookie", 2, 480)

# Order items
restaurant2.customer_order(51,"Cinnamon Roll, Twisted Churro")
restaurant2.customer_order(57,"Chocolate Chip Cookie")
restaurant2.customer_order(87,"Twisted Churro")
restaurant2.customer_order(93,"Cinnamon Roll")

print("\nPopular dishes in the restaurant along with their prices:")
restaurant2.print_menu_items()

print("\nPrint customer orders:")
restaurant2.print_customer_orders()