#Authur AmirArab
# What needed for whole program
import datetime
### What I have learnt from Class: os / export
import os
from tabulate import tabulate
import sqlite3 as db
db = db.connect('Lib.db')
lib = db.cursor()

Today = datetime.datetime.now()
twoWeeks = Today + datetime.timedelta(weeks=2)


def show_books():
    lib.execute('''
            select * from Books
            ''')
    all_rows = lib.fetchall()
    lists = list(all_rows)
    names = [description[0] for description in lib.description]
    books = tabulate(lists, headers=names)
    print(books)


def show_members():
    lib.execute('''
            select * from Members
            ''')
    all_rows = lib.fetchall()
    lists = list(all_rows)
    names = [description[0] for description in lib.description]
    print(tabulate(lists, headers=names))


def tables():
    print(tabulate([
        ['[1]', 'Books'], ['[2]', 'Members']], headers=['Nubmer*', 'Table']))




# Outputs
def lib_main():
    # The very beginnig
    os.system('cls')
    print(tabulate([
        ['[1]', 'Insert', ' Putting new datum in the Library Database'],
        ['[2]', 'Read/Save', ' Show/Save datum in the database tables'],
        ['[3]', 'Delete', ' Delete entire row in tables'],
        ['[4]', 'Update', 'Make some changes to an existing row'],
        ['[0]', 'Quit', 'Quit from all commitments']],
        headers=['Nubmer*', 'Command', 'Comment']))

    answer = input(
        '\n Select What you want to do from above. Just CHOOSE THE NUMBER: ')

    if answer == '1':
        tables()
        insert_ans = input(
            '\n In which table you want to add a row? Just CHOOSE THE NUMBER: ')
        if insert_ans == '1':
            show_books()
            lib.execute('''
                INSERT INTO Books(Title, Author, ISBN) VALUES(:Title, :Author, :ISBN)''',
                        {'Title': input("Title: "),
                         'Author': input("Author: "),
                         'ISBN': input("ISBN: "),
                         })
        elif insert_ans == '2':
            show_members()
            lib.execute('''
                INSERT INTO Members(IDNumber, Name, LastName, PhoneNumber, RegisterDate)
                VALUES(:IDNumber, :Name, :LastName, :PhoneNumber, :RegisterDate)''',
                        {'IDNumber': input("ID_Number: "),
                         'Name': input("Name: "),
                         'LastName': input("Last_Name: "),
                         'PhoneNumber': input('Phone_Number: '),
                         'RegisterDate': Today})
        db.commit()

    if answer == '2':
        tables()
        read_ans = input(
            '\n Which table you want to see? Just CHOOSE THE NUMBER: ')
        if read_ans == '1':
            lib.execute('''
                        select * from Books
                        ''')
            all_rows = lib.fetchall()
            lists = list(all_rows)
            names = [description[0] for description in lib.description]
            books = tabulate(lists, headers=names)
            print(books)
            ask_save = input('\nDo you want to Export to a TxtFile [y/n]? ')
            if ask_save.upper().lower().startswith("y"):
                file = open('Books.txt','w')
                file.write(books)
                file.close()
                print('\n It is done :) ')
            else:
                pass
        elif read_ans == '2':
            lib.execute('''
                        select * from Members
                        ''')
            all_rows = lib.fetchall()
            lists = list(all_rows)
            names = [description[0] for description in lib.description]
            members = tabulate(lists, headers=names)
            print(members)
            ask_save = input('\nDo you want to Export to a TxtFile [y/n]? ')
            if ask_save.upper().lower().startswith("y"):
                file = open('Members.txt','w')
                file.write(members)
                file.close()
                print('\n It is done :) ')
            else:
                pass

    if answer == '3':
        tables()
        del_ans = input(
            "\n Which tables row you want to delete? Just CHOOSE THE NUMBER: ")
        if del_ans == '1':
            show_books()
            lib.execute('''
                delete from Books where RowID = ?''',
                        (input('RowID: '),)
                        )
        if del_ans == '2':
            show_members()
            lib.execute('''
                delete from Members where RowNo = ?''',
                        (input('RowNo: '),)
                        )
    if answer == '4':
        print(" \n oooops, it is not accessible yet!!! ")

    db.commit()

    ask = input('\nYou have finished the script.\nDo you want to start again [y/n]? ')
    if ask.upper().lower().startswith("y"):
        lib_main()

    else:
        print('Thanks for using this script')

    if answer == '0':
        print('Thanks for using this script')



lib_main()
db.close()
