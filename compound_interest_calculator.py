principle = 0
rate = 0
time = 0
while principle <= 0:
    principle = float(input("Enter the principle amount: "))    
    if principle <= 0:
        print("Principle amount must be greater than zero. Please enter a valid amount.")

while rate <= 0:
    rate = float(input("Enter the annual interest rate (in percentage): "))
    if rate <= 0:
        print("Interest rate must be greater than zero. Please enter a valid rate.")

while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time must be greater than zero. Please enter a valid time.")
        
total_amount = principle * pow(1 + (rate / 100), time)
print(f"The total amount after {time} years is: {total_amount:.2f}")
