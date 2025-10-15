
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""


def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}!")

def main():
    user_name = get_user_name()
    greet_user(user_name)

if __name__ == "__main__":
    main()

def contains_digits():
    #loop through characters in string
    # if digit return true
    # return false if no digits found
    # stop if digit found
    # if seperate strings check each string

    # "hello" -> False
    # "hello123" -> True
   #Input: a string (not from user)
    # returns: boolean (True/False)
    # for each character in string
    statuses = {"Santiago": "online", "Sasha": "online", "Ezekiel": "online", "Julianna": "online"}

    def online_count(statuses):
     status_count = 0
    for name in statuses:
            status = statuses[name]
            if status == "online":
                status_count +=1
    return (status_count)
print (online_count(statuses))
