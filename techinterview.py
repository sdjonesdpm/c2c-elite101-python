# Write a function to determine the number of vowels in a string
def count_vowels(user_input):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    for char in user_input:
        if char in vowels:
            vowel_count += 1
    return vowel_count
print(count_vowels(user_input = input("Hello, please enter a string and I'll count the vowels!")))
