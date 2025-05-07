tableNumber = int(input("Enter a number to generate its multiplication table: "))

for i in range(1, 11):
    print(f"{tableNumber} x {i} = {tableNumber * i}")

print("Multiplication table generated successfully!")