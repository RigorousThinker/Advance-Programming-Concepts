file = open("transactions.txt", "r")

deposits = 0
withdrawals = 0
largest = 0

for line in file:
    transaction, amount = line.strip().split(",")
    amount = float(amount)

    if transaction == "deposit":
        deposits += amount
    elif transaction == "withdrawal":
        withdrawals += amount

    if amount > largest:
        largest = amount

file.close()

balance = deposits - withdrawals

print("Total deposits:", deposits)
print("Total withdrawals:", withdrawals)
print("Final balance:", balance)
print("Largest transaction:", largest)