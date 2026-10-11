print("===== TIP CALCULATOR =====")

bill = float(input("Enter bill amount: ₹"))
gst = float(input("Enter GST percentage: "))
tip = float(input("Enter tip percentage: "))

gst_amount = bill * gst / 100
tip_amount = bill * tip / 100

total = bill + gst_amount + tip_amount

print("\n===== BILL SUMMARY =====")
print(f"Bill Amount: ₹{bill:.2f}")
print(f"GST Amount: ₹{gst_amount:.2f}")
print(f"Tip Amount: ₹{tip_amount:.2f}")
print(f"Total Amount: ₹{total:.2f}")
