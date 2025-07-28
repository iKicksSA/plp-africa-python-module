# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.

def calculate_discount(price,discount_percent):

  discounted_amount = price * discount_percent / 100
  after_discount = price - discounted_amount

  if discount_percent >= 0 and discount_percent <= 100:
    print(f"After a {discount_percent}% discount, you should pay R{after_discount} only.")

  else:
    print(f"Discount can\'t be above 100% ")

original_price = int(input("Enter a price of an item: R "))
discount = int(input("Enter a discount for that item if available, enter ZERO if it\'s not: "))

calculate_discount(original_price,discount)