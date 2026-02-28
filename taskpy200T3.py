# PY200_T3 — Electricity bill slab
# Author  : Akanksha Singh

units = int(input("Enter electricity units consumed: "))

bill = 0

if units > 0:
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + ((units - 100) * 3)
    elif units <= 500:
        bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)
    else:
        bill = (100 * 2) + (100 * 3) + (300 * 5) + ((units - 500) * 8)

    bill += 50  # Fixed charge

# PY200T3 - Electricity bill slab calculation

# Input unit
units = int(input("Enter units: "))

bill = 0

if units > 0:
    # First 100 units
    if units >= 100:
        bill += 100 * 2
        units -= 100
    else:
        bill += units * 2
        units = 0

    # Next 100 units
    if units > 0:
        if units >= 100:
            bill += 100 * 3
            units -= 100
        else:
            bill += units * 3
            units = 0

    # Next 300 units
    if units > 0:
        if units >= 300:
            bill += 300 * 5
            units -= 300
        else:
            bill += units * 5
            units = 0

    # Above 500 units
    if units > 0:
        bill += units * 8

    # Fixed charge
    bill += 50

print("Total Bill =", bill)