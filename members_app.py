
import csv
from pathlib import Path
import pandas as pd

class _defaults:
    name_csv = 'members.csv'


def __addNewMember() -> None:
    print(f"Dates of new member:")
    name = str(input(f"Name: "))
    last_name = str(input(f"Last name: "))
    email = str(input(f"Email: "))
    birthdate = str(input(f"Birthdate: "))

    # Verificar si el archivo ya existe
    if not Path(_defaults.name_csv).is_file():
        # Si el archivo no existe, crearlo y escribir los datos
        with open(file = _defaults.name_csv, mode = 'w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=',')
            writer.writerow(['name', 'last name', 'email', 'birthdate'])
            writer.writerow([name, last_name, email, birthdate])
    else:
        with open(file = _defaults.name_csv, mode = 'a', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=',')
            writer.writerow([name, last_name, email, birthdate])
    print(f"Member added\n")


def __deleteMember() -> None:
    try:
        member_email = input(f"Enter the email of the member you want to delete: ")
        df = pd.read_csv(_defaults.name_csv)
        emails = df['email'].values.tolist()
        if member_email in emails:
            position = emails.index(member_email)
            df = df.drop(position, axis = 0)
            df.to_csv(_defaults.name_csv, index=False)
            print(f"Deleted member\n")
        else:
            print('Member no exist\n')
    except:
        print('Invalid email')


def __showMembers() -> None:
    try:
        df = pd.read_csv(_defaults.name_csv)
        print(f"{df}\n")
    except:
        print(f"No members\n")


def main():
    election = 0
    while election != 4:
        election = input(f"Choose one of the following options:\n1. Add member.\n2. Delete member.\n3. Show all members.\n4. Exit\nOption: ")
        print(f"\n")
        try:
            election = int(election)
            if election == 1:
                __addNewMember()
            elif election == 2:
                __deleteMember()
            elif election == 3:
                __showMembers()
            elif election == 4:
                print(f"Goodbye")
            else:
                print(f"Invalid election")
        except:
            print(f"Invalid election")

if __name__ == '__main__':
    main()