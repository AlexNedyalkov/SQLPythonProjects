from ProgDiary.database import create_table, add_entry, get_entries

menu = """Please select: 
        1) Add new entry for today. 
        2) View entries
        3) Exit

Your selection: """

welcome = 'Welcome to the program diary'

def prompt_new_entry():
    entry_content = input('What have you learned today?')
    date_content = input('Enter the date: ')
    add_entry(entry_content, date_content)

def view_entries():
    for entry in get_entries():
        print(f'{entry["date"]}\n{entry["content"]}\n\n')

print(welcome)
create_table()

user_input = input(menu)

while user_input != 3:
    if user_input == '1':
        prompt_new_entry()
    elif user_input == '2':
        view_entries()
    elif user_input == '3':
        break
    else:
        print('Invalid option, please try again!')
    user_input = input(menu)

