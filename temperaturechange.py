while True: 
   unit = input("What unit of temperature do you want to convert? Enter c for Celsius, f for Fahrenheit, or q to quit: ")
   unit = unit.upper()
   print(unit)
   if unit == "Q":
        print("All the best and have a nice day")
        break
   try:
     if unit not in ["C", "F"]:
       raise ValueError("Invalid unit of temperature. Please enter c for Celsius or f for Fahrenheit.")
   except ValueError as e:
     print(e)
     continue
   temp_input = input(f"Enter the temperature in {unit.capitalize()}: ")
   try:
     temp = float(temp_input)
   except ValueError:
     print("Invalid temperature. Please enter a numeric value.")
     continue
   if unit == "C":
     temp_in_fahrenheit = (temp * 9/5) + 32
     print(f"{temp} degree Celsius is equal to {temp_in_fahrenheit} degree Fahrenheit")
   elif unit == "F":
     temp_in_celsius = (temp - 32) * 5/9
     print(f"{temp} degree Fahrenheit is equal to {temp_in_celsius} degree Celsius")
   else:
     print("Invalid unit of temperature. Please enter c for Celsius or f for Fahrenheit.")
