def change_due(amount_paid, total_bill):
    return amount_paid - total_bill
total_bill = float(input("Enter the total bill amount: $"))
amount_paid = float(input("Enter the amount you paid: $"))
change = change_due(amount_paid, total_bill)
print(f"You will recieve: ${change:.2f}")