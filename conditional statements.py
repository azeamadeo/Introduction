temperature = int(input("Enter the temperature in Celsius: "))

if temperature < 20:
    outfit = "jacket"
    print("It's cold outside. Wear a", outfit)
else:
    outfit = "t-shirt"
    print("It's warm outside. Wear a", outfit)

is_raining = input("Is it raining? (yes/no): ")

if is_raining.lower() == "yes":
    print("bring an umbrella!")
else:
    is_raining.lower() == "no"
    print("no need for an umbrella today.")

wind_speed = int(input("Enter the wind speed in km/h: "))

if wind_speed > 30:
        needs_windbreaker = "yes"
        print("It's windy. You should wear a windbreaker over your", outfit)
else:
     needs_windbreaker = "no"
     print(" it is calm today. No need for a windbreaker over your", outfit, ".")

has_puddles = input("Are there puddles on the ground? (yes/no): ")

if has_puddles == "yes":
    shoes = "boots"
    print("the ground is wet. Wear", shoes)

    print("")
    print("weather check complete")

else:
    shoes = "sneakers"
    print("the ground is dry. Wear", shoes)

    print("==== WEATHER OUTFIT PICKER ====")
    print("Temperature:", temperature, "°C")
    print("outfit chosen:", outfit)
    print("raining:", is_raining)
    print("windbreaker needed:", needs_windbreaker)
    print("shoes chosen:", shoes)
    print("==========================================")
