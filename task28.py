from getpass import getpass

password = getpass()

result = password == 'secret' and password == ''

print(result)