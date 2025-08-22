def calculate_discount(price, discount_percent):
  """
  Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percent: The discount percentage (e.g., 20 for 20%).

  Returns:
    The final price after applying the discount, or the original price if the discount is less than 20%.
  """
  if discount_percent >= 20:
    discount_amount = (discount_percent / 100) * price
    final_price = price - discount_amount
    return final_price
  else:
    return price

# Get user input
try:
  price = float(input("Enter the original price of the item: "))
  discount_percent = float(input("Enter the discount percentage: "))
except ValueError:
  print("Invalid input. Please enter numeric values for price and discount percentage.")
  exit()

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the result
if final_price == price:
  print("No discount applied. The final price is:", price)
else:
  print("The final price after applying the discount is:", final_price)
