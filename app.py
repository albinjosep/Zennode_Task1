# Import the 're' module for regular expressions
import re

# Define a Catalogue class
class Catalogue:
    def __init__(self):
        # Initialize the products and their prices
        self.products = {
            "Product A": 20,
            "Product B": 40,
            "Product C": 50
        }

    def calculate_discount(self, cart_total, quantities):
        # Initialize the discount amount
        discount_amount = 0

        # Apply a discount if the cart total is greater than 200
        if cart_total > 200:
            discount_amount = min(discount_amount + 10, cart_total)

        # Check if the quantity for each product is greater than 10
        for product, quantity in quantities.items():
            if quantity > 10:
                discount_amount += self.products[product] * quantity * 0.05

        # Calculate a discount based on the total quantity
        total_quantity = sum(quantities.values())
        if total_quantity > 20:
            discount_amount = min(discount_amount + cart_total * 0.1, cart_total)

        # Apply additional discount for quantities greater than 30
        if total_quantity > 30:
            for product, quantity in quantities.items():
                if quantity > 15:
                    discount_amount += (quantity - 15) * self.products[product] * 0.5

        # Return the total discount amount
        return discount_amount

    def shipping_fee(self, total_quantity):
        # Calculate shipping fee based on total quantity
        return (total_quantity // 10) * 5

    def process_order(self):
        # Initialize quantities and gift wrap fee
        quantities = {}
        gift_wrap_fee = 0

        # Loop through each product to get quantity and gift wrapping information
        for product in self.products:
            quantity = int(input(f"Enter the quantity for {product}: "))

            # Validate user input for gift wrapping
            pattern = r"^(yes|no)$"
            while True:
                response = input(f"Is {product} wrapped as a gift? (YES/NO): ").lower()
                if re.match(pattern, response):
                    is_gift_wrapped = response == "yes"
                    break
                else:
                    print("Invalid input. Please enter 'YES' or 'NO'.")

            # Update quantities and gift wrap fee
            quantities[product] = quantity
            if is_gift_wrapped:
                gift_wrap_fee += quantity

        # Calculate subtotal, discount, shipping fee, and total
        subtotal = sum(self.products[product] * quantities[product] for product in self.products)
        discount_amount = self.calculate_discount(subtotal, quantities)
        shipping_fee = self.shipping_fee(sum(quantities.values()))
        total = subtotal - discount_amount + shipping_fee + gift_wrap_fee

        # Display order summary
        print("\nOrder Summary:")
        for product, quantity in quantities.items():
            subtotal_per_product = self.products[product] * quantity
            print(f"{quantity} {product}s - Subtotal: ${subtotal_per_product}")

        details = f"""
        Subtotal: ${subtotal}
        Discount Applied: ${discount_amount}
        Shipping Fee: ${shipping_fee}
        Gift Wrap Fee: ${gift_wrap_fee}
        Total: ${total} 
        """
        
        print(details)


# Example usage
catalogue = Catalogue()
catalogue.process_order()
