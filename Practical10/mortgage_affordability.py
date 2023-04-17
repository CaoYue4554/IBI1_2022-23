def house(value,salary):
    buy = "No"
    if 5*salary >= value:
        buy = "Yes"
    return buy
print(house(180000,35000))
