# jean 24/02/2022
import os
import time

# Clearing the Screen
# posix is os name for linux or mac
if os.name == 'posix':
    os.system('clear')
# else screen will be cleared for windows
else:
    os.system('cls')

print('<Pass BruteForce Test>')
print('Esse programa destina-se a testar uma senha em relação a um dicionário de senhas')
print('--------------')
# Printing the os name
print("os name is :", os.name)
print('-------------- (c)02/2022 - jean \n\n')

senha = input('Digite a senha a testar: ')

# https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt
dictionary = '10-million-password-list-top-1000000.txt'
# dictionary = 'dictionary_teste.txt'

file = open(f'{dictionary}', 'r')

print('Aguarde ! Lendo as senha no dicionário: ', dictionary)
bruteforce = []
for line in file:
    line = line.strip()
    bruteforce.append(line)
file.close()

print('Quantidade de senhas no dicionário: ', len(bruteforce))

time.sleep(2)  # secs

input('Tecle algo para iniciar !!!')

print('INÍCIO da execução !')
matchs = 0
linha = 0
for testa in bruteforce:
    linha += 1
    # print(f'> linha {linha}: {testa}')
    if testa == senha:
        print('MATCH da senha na linha: ', linha)
        matchs += 1

if matchs == 0:
    print('nenhum MATCH !')

print('FIM da execução !')
quit()
