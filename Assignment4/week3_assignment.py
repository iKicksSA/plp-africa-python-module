
def calculate_discount(price,discount_percent):

  discounted_amount = price * discount_percent / 100
  after_discount = price - discounted_amount

  if discount_percent >= 0 and discount_percent <= 100:
    print(f"After a {discount_percent}% discount, you should pay R{after_discount} only.")

  else:
    print(f"Discount can\'t be above 100% ")
