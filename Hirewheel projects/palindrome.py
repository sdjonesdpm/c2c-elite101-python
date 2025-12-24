#We must determine if a given string is a palindrome.
#Convert to lowercase and ignore weird characters like spaces and punctuation.
#handle edge cases, including empty strings, mixed cases, or inputs with symbols.
#Return a clear message that indicates whether a string is a palindrome.
s = input("Please enter a string to test if it is a palindrome:")

reverse = s[::-1]

if s == "":
    print("The empty string is considered a palindrome.")

elif not s.isalnum():
    print(f"{s} is a palindrome with non-alphanumeric characters.")

elif s.lower() == reverse.lower():
    print(f"{s} is a palindrome.")

elif ' ' in s or not s.isalnum():
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    cleaned_reverse = cleaned_s[::-1]
    if cleaned_s == cleaned_reverse:
        print(f"{s} is a palindrome when spaces and punctuation are ignored.")
    else:
        print(f"{s} is not a palindrome.")

elif reverse == s:
    print(f"'{s}' is a palindrome!")

else: print(f"{s} is not a palindrome.")


#another elif is needed to ignore spaces
