word = (input("Enter a word in which you would like to find vowels in: "))
for x in word:
    if x in "aeiouAEIOU":
        print(x.capitalize() + " is a vowel.")
