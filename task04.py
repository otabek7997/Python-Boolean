from getpass import getpass

password = getpass("Enter password: ")
result = len(password) >= 8

print(result)