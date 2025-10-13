print("Hi! My name is Helping Handy and I am here to assist you today.")
name = input("What is your name?")
print(f"Nice to meet you {name},")
order = input("how old are you?")
print("Welcome in! How can I help you today?\n")

options = ['1. Option 1', '2. Option 2', '3. Option 3', '4. Exit the conversation']
print("\n".join(options))
number = input("Please choose from the following options:")
if number == '4':
    print("Later! See you next time!")
