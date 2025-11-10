def bot():
    print("Hi! My name is Helping Handy and you have entered Manny's Tex-Mex Eatery.")
name = input("What is your name?")
print(f"Nice to meet you {name},")
age_input = input("People of a certain age recieve discounts!\n How old are you?")
age = int(age_input)
if age < 18:
    print("You get 30% off your first order!\n")
elif age >18:
    print("Sorry, Looks like you don't qualify for a discount today.")
else:
    print("Please input a valid age.")

print("How can I help you today?\n")

options = ['1. Store Hours', '2. Location', '3. Available Products', '4. Prices', '5. Exit']
print("\n".join(options))
number = input("Please choose from the following options:")
if number == '5':
    print("Later! See you next time!")
    exit()
elif number == '1':
    print("We are open 24hrs a day, Monday through Saturday!")
elif number == '2':
    print("We are located at 512 Wigglesburg Ln, Austin, TX 01410")
elif number == '3':
    print("We have a variety of Tex-Mex foods:\n")
    products = ['Tacos\n', 'Burritos\n', 'Quesadillas\n','Sharable Nachos\n', 'Fajitas\n', 'Chips & Salsa\n']
    for item in products:
        print(item)
elif number == '4':
    print("Our prices have been affordable since 1738!/n Here is a list of our prices per item:")
prices = ['Tacos: 3.50 each', 'Burritos: 4.50 each', 'Quesadillas: 2.00 each', 'Sharable Nachos: 5.00 each', 'Fajitas: 6.50 each', 'Chips & Salsa: 1.50 each']
for price in prices:
    print(price)
#def goodbye():
    #print("Do you need anything else today?")
    #bye_input = input("Please enter Y for Yes")
    #if bye_input.lower() == 'y':
        #print("How else can I assist you today?")
    #else :
        #print("Thank you for talking with me! Have a great day!")
