from getpass import getpass

password = getpass("Write the password: ")
confirm = getpass("Confirm the password: ")

result = password == confirm

print(result)