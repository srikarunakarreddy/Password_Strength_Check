import string


def strong_password(password):
    if len(password) < 8:
       return "Password must be at least 8 characters long"
    if " " in password:
        return "Password must not contain spaces"

    has_upper = any(char.isupper() for char in password)
    has_lower = any(chat.islower() for chat in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if all([has_upper, has_lower, has_digit, has_special]):
        return "Your Password is strong"
    else:
        return "Your Password is not strong"
while True:
        user_password = input("Enter your password(or type 'exit' to quit): ")
        if user_password.lower() == "exit":
            print("Goodbye!")
            break
        output = strong_password(user_password)
        print(output)
