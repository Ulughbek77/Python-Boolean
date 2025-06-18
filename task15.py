from getpass import getpass

password = getpass("Enter your password: ")
confirm = getpass("Confirm your password: ")

result = password == confirm
print(result)