# jean modesto 02/2022
import os
import time

# Clearing the Screen
# posix is os name for linux or mac
if os.name == 'posix':
    os.system('clear')
# else screen will be cleared for windows
else:
    os.system('cls')

print('<Testing Passwords>')
print('------------------- (c)02/2022 - https://github.com/jeanmodesto \n\n')

user_pass = input('Type the password to test: ')

# https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt
dictionary = '10-million-password-list-top-1000000.txt'
# dictionary = 'dictionary_teste.txt'

file = open(f'{dictionary}', 'r')

print('Please wait! Readind dictionary: ', dictionary)
bruteforce = []
for line in file:
    line = line.strip()
    bruteforce.append(line)
file.close()

time.sleep(2)  # secs

print('Dictionary lenght: ', len(bruteforce))

input('\n(Press any key to continue)')

print('BEGIN...')
matchs = 0
linha = 0
for dict_pass in bruteforce:
    linha += 1
    # print(f'> linha {linha}: {testa}')
    if dict_pass == user_pass or dict_pass.upper() == user_pass or dict_pass.lower() == user_pass or\
            dict_pass.capitalize() == user_pass:
        print(f'>>> MATCH found on line: {linha}, value: {dict_pass}')
        matchs += 1

if matchs == 0:
    print('>>> NO MATCH IN DICTIONARY !')

print('END...')
quit()
