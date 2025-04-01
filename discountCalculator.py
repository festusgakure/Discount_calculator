def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price after discount
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied, return the original price
        return price


# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = int(input("Enter the discount percentage: "))

# Apply the discount and print the final price
final_price = calculate_discount(original_price, discount_percent)
if final_price != original_price:  # If discount was applied
    print(f"The final price after applying the discount is: Ksh{final_price:.2f}")
else:  # No discount applied
    print(f"The original price is: Ksh{original_price:.2f} (No discount applied as it is less than 20%)" )