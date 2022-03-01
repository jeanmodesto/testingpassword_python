# https://github.com/jeanmodesto
# (c) 02/2022, 03/2022
#
# Dictionary:
# https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt
from tkinter import *
import time

root = Tk()
root.geometry("600x300")
root.title('Testing Password Vr. 0.1')
# não permite mudar o tamanho da janela
root.resizable(False, False)

# calcula a fim de centralizar a janela do app na tela
window_width = 600
window_height = 400
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# create a menubar
menubar = Menu(root)
root.config(menu=menubar)
# create a menu
option1_menu = Menu(menubar, tearoff=False)
# add the File menu to the menubar
menubar.add_cascade(
    label="Menu",
    menu=option1_menu
)
# add a menu item to the menu
option1_menu.add_command(
    label='Exit',
    command=root.destroy
)

# frame dos forms
frame = Frame(root)

# field options
options = {'padx': 5, 'pady': 5}

# input do dictionary filename
label_dictionary_filename = Label(frame, text="Type the dictionary filename (example: dictionary.txt):",
                                  font="calibri 10")
label_dictionary_filename.grid(column=0, row=2, sticky='W', **options)
dictionary_filename = StringVar()
dictionary_filename_entry = Entry(frame, textvariable=dictionary_filename)
dictionary_filename_entry.grid(column=0, row=3, **options)
dictionary_filename_entry.insert(0, 'dictionary.txt')  # default value
# dictionary_filename_entry.focus()

# input da senha de teste
label_pass_test = Label(frame, text="Type the password to test:", font="calibri 10")
label_pass_test.grid(column=0, row=5, sticky='W', **options)
pass_test = StringVar()
pass_test_entry = Entry(frame, textvariable=pass_test)
pass_test_entry.grid(column=0, row=6, **options)
pass_test_entry.focus()

# status label
status_label = Label(frame)
status_label.grid(row=12, column=0, **options)

# result label
result_label = Label(frame)
result_label.grid(row=14, column=0, **options)


def run_button_clicked():
    dict_filename = dictionary_filename.get()
    print('Dictionary filename:', dict_filename)
    if dict_filename.strip() == '':
        status_label.config(text='Dictionary filename is required !!!')
        return

    user_pass = pass_test.get()
    print('Pass:', user_pass)
    if user_pass.strip() == '':
        status_label.config(text='Password is required !!!')
        return

    try:
        file = open(f'{dict_filename}', 'r')
    except IOError:
        txt = f">>> DICTIONARY FILE NOT FOUND: {dict_filename} !!!"
        status_label.config(text=txt)
        print(txt)
        return

    # inicia leitura do arquivo
    print('\nBEGIN...')
    time.sleep(1)  # secs

    bruteforce = []
    for line in file:
        line = line.strip()
        bruteforce.append(line)

    file.close()

    bruteforce_len = len(bruteforce)
    txt = f">>> Dictionary lines: {bruteforce_len} !!!"
    status_label.config(text=txt)
    print(txt)

    # input('\n(Press any key to continue)')

    matchs = 0
    i = 0
    for dict_pass in bruteforce:
        i += 1
        if dict_pass == user_pass or dict_pass.upper() == user_pass or dict_pass.lower() == user_pass or\
                dict_pass.capitalize() == user_pass:
            txt = f'>>> MATCH found on line: {i}, value: {dict_pass}'
            status_label.config(text=txt)
            print(txt)
            matchs += 1

    if matchs == 0:
        txt = ">>> PASS NOT FOUND IN DICTIONARY !"
    else:
        txt = f">>> PASS MATCHS IN DICTIONARY: {matchs}"

    result_label.config(text=txt)
    print(txt)

    print('\nEND...')
    return


run_button = Button(frame, text='Run Test')
run_button.grid(column=0, row=7, sticky='W', **options)
run_button.configure(command=run_button_clicked)

disclaimer = Label(frame, text="Disclaimer: for educational purposes only", font="calibri 6")
disclaimer.grid(column=0, row=100, sticky='W', **options)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)
root.mainloop()
