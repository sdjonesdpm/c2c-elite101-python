#We must determine if a given string is a palindrome.
#Convert to lowercase and ignore weird characters like spaces and punctuation.
def find_palindrome(s):
if not isinstance(s, str):
    return "Input has to be a string"
s=s.lower()
