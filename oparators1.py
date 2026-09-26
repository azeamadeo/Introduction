field1 =120
field2 =85
field3 = 100
field4 = 90
field5 = 95

total = field1 + field2 + field3 + field4 + field5

average = total / 5

print("total harvest        :",total, "kg")
print("average harvest      :",average, "kg")

price_per_kg = 15
earnings = total * price_per_kg
print("total earnings       :Rs.",earnings)

bags = total // 25
leftover = total % 25

print("total bags packed  :",bags)
print("leftover grain   :",leftover, "kg")

last_year = 500
print("better than last year?  :",total > last_year)
print("same as last year?      :",total == last_year)
print("worse than last year?   :",total < last_year)

total += 30
print("after bonus crop  :",total, "kg")
total -= 15
print("after seed reserve  :",total, "kg")

bags = total // 25
print("final bags packed  :",bags)