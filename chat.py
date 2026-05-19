name = input("What is your name? ")
print(f"Hello, {name}! Welcome to the chat.")

age = int(input("How old are you? "))

if age < 18:
    print("Nice! You are still a young person.")
elif age < 50:
    print("Great! You are in the prime of your life.")
else:
    print("Wonderful! You have a lot of experience.")

print(f"Great! You are {age} years old.")
