print("===== TIP CALCULATOR =====")

bill = float(input("Enter bill amount: ₹"))
tip = float(input("Enter tip percentage: "))

tip_amount = bill * tip / 100
total = bill + tip_amount

print("\n===== BILL =====")
print("Bill:", bill)
print("Tip:", tip_amount)
print("Total:", round(total, 2))