from getpass import getpass

code = str('secret123')

password = str(getpass("Enter the password: "))
result = password == code

print(result)