print("ELECTRICITY BILL CALCULATOR")
houses = ["House 1", "House 2", "House 3"]
for house in houses:
    print("\n", house)

    total_units=0
    for month in ["January", "February", "March"]:
        units=int(input("Enter units for "+ month + ": "))
        total_units += units

    bill = total_units * 5

    print("Total units", total_units)
    print("Electricity Bill: $", bill)

choice = "yes"
while choice == "yes":
    print("\nThank you for using the calculator!")

    choice = input("Calculate again? (yes/no): ").lower().strip()