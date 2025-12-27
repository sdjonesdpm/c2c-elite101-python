def acronym_generator():
    # Prompt the user for a phrase or sentence.
    phrase = input("Please enter a phrase or sentence: ")
    # Split the phrase into words (ignore blank segments or punctuation).
    words = [word for word in phrase.split() if word.isalpha()]
    # Collect the first letter of each word, uppercase it, and join into the final acronym.
    acronym = ''.join(word[0].upper() for word in words)
    # Handle edge cases such as empty input or single-word phrases gracefully.
    if not acronym:
        print("No valid words found.")
        return
    print(f"The acronym for '{phrase}' is: {acronym}")
acronym_generator()
