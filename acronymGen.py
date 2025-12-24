def acronym_generator():
# Prompt the user to enter a phrase
    prompt = input("Please enter a phrase and I'll generate its acronym:")
#Spilt the phrase into words(ignore blank segments or punctuactions)
    words = [word for word in prompt.split() if word.isalnum()]
#Collect the first letter of each word, uppercase it, and join into the final acronym
    acronym = ''.join(word[0].upper()for word in words)

    print(f"The acronym for '{prompt}' is: {acronym}")

    print("hello")
