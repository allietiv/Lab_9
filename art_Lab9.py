

def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str(int(digit) + 3)
        encoded_password += encoded_digit
    return encoded_password

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")  # Assuming you'll add this functionality later
        print("3. Quit")
        print()
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            return
        elif option == 3:
            break

if __name__ == "__main__":
    main()