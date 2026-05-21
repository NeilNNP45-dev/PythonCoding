while True: 
   unit = input("What unit of temperature do you want to convert? Enter c for Celsius, f for Fahrenheit, or q to quit: ")
   print(unit)
   if unit == "q":
        print("All the best and have a nice day")
        break
   temp_input = input(f"Enter the temperature in {unit.capitalize()}: ")
   try:
     temp = float(temp_input)
   except ValueError:
     print("Invalid temperature. Please enter a numeric value.")
     continue
   if unit == "c":
     temp_in_fahrenheit = (temp * 9/5) + 32
     print(f"{temp} degree Celsius is equal to {temp_in_fahrenheit} degree Fahrenheit")
   elif unit == "f":
     temp_in_celsius = (temp - 32) * 5/9
     print(f"{temp} degree Fahrenheit is equal to {temp_in_celsius} degree Celsius")
   else:
     print("Invalid unit of temperature. Please enter c for Celsius or f for Fahrenheit.")
