def bot():
    print("Hi! My name is Helping Handy and you have entered Manny's Tex-Mex Eatery.")
name = input("What is your name?")
print(f"Nice to meet you {name},")
age_input = input("How old are you?")
age = int(age_input)
if age < 18:
    print("You get 30% off your first order!")

print("How can I help you today?\n")

options = ['1. Store Hours', '2. Location', '3. Available Products', '4. Prices', '5. Exit']
print("\n".join(options))
number = input("Please choose from the following options:")
if number == '5':
    print("Later! See you next time!")
elif number == '1':
    print("We are open 24hrs a day, Monday through Saturday!")
elif number == '2':
    print("We are located at 512 Wigglesburg Lanes, Austin, TX 01410")
elif number == '3':
    print("We have a variety of Tex-Mex foods\n")
    products = ['Tacos', 'Burritos', 'Quesadillas','Sharable Nachos', 'Fajitas', 'Chips & Salsa']
    print("/n".join(products))
elif number == '4':
    print("Our prices have been affordable since 1738!/n Here is a list of our prices per item:")
prices = ['Tacos: 3.50 each', 'Burritos: 4.50 each', 'Quesadillas: 2.00 each', 'Sharable Nachos: 5.00 each', 'Fajitas: 6.50 each', 'Chips & Salsa: 1.50 each']
