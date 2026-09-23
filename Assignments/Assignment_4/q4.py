item = "Soda"
unit_price = 3.45
quantity = 4
tax_rate = 0.05
subtotal = (unit_price*quantity)
tax_amount = (subtotal*tax_rate)
final_total = (subtotal + tax_amount)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"Final Total: ${final_total:.2f}")
