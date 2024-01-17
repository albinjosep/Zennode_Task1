# Catalogue Processing System

This Python program represents a basic catalogue processing system that allows users to input quantities for different products and specify if they want gift wrapping for each product. The system calculates the order summary, including subtotal, discounts, shipping fees, and total cost.

## Usage

1. Run the Python script.
2. Enter the quantity for each product when prompted.
3. Specify if the product should be wrapped as a gift by entering 'YES' or 'NO' when prompted.
4. The program will display the order summary, including subtotals, discounts, shipping fees, gift wrap fees, and the total cost.

## Catalogue Class

- The `Catalogue` class contains methods for calculating discounts (`calculate_discount`), determining shipping fees (`shipping_fee`), and processing the entire order (`process_order`).
- Products and their prices are initialized in the class constructor.

## Input Validation

- The program uses regular expressions to validate user input for gift wrapping, ensuring only 'YES' or 'NO' responses are accepted.

Feel free to customize the catalogue, prices, and discount rules based on your specific requirements.
