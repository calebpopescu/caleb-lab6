# Name: Caleb Popescu

def encode_password(password):
    encoded_password = ""
    for digit in password:
        shifted_digit = str((int(digit) + 3) % 10)  # shift each digit up 3 numbers
        encoded_password += shifted_digit
    return encoded_password

def decode_password(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        shifted_digit = str((int(digit) - 3) % 10)  # shift each digit down 3 numbers
        decoded_password += shifted_digit
    return decoded_password

# main program loop
while True:
    print("Menu")
    print('-------------')
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    choice = input("Please enter an option: ")

    if choice == "1":
        password = input("Please enter your password to encode: ")
        encoded_password = encode_password(password)
        print("Your password has been encoded and stored!")
    elif choice == "2":
        encoded_password = input("Please enter your encoded password to decode: ")
        decoded_password = decode_password(encoded_password)
        print("The encoded password is {}, and the original password is {}.".format(encoded_password, decoded_password))
    elif choice == "3":
        break
    else:
        print("Invalid option. Please try again.")
