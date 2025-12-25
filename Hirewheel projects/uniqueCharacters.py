# Create a function that checks whether all characters in a string are unique.

def unique_characters(s):
    # Return True if the string contains only unique characters; otherwise return False.
    return len(set(s)) == len(s)


if __name__ == "__main__":
    s = input("Enter a string and I'll check if it has all unique characters: ")

    if not s:  # Handle empty strings
        print("The string is empty.")
    elif not s.isalnum() and s.strip(): # Check if it contains non-alphanumeric characters (not just spaces)
        print(f"The string contains non-alphanumeric characters. Result using case-sensitive check: {unique_characters(s)}")
    elif s != str(): # address non-string inputs
        print("Invalid input. Please enter a valid string.")
    else:
        result = unique_characters(s) #print result to user
        print(f"The result is: {result}")
