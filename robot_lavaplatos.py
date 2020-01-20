plate_list = []
def add_plate():
    global plate_list
    plate_list.append("\___/")

def show_plate_list():
    global plate_list
    if len(plate_list) == 0:
        print('No hay platos en el lavaplatos ')
    plate = '   \___/'
    for i in plate_list:
        print(plate)



def wash_plate():
    global plate_list
    if len(plate_list) == 0:
        print('No hay platos para lavar ')
    else:
        plate_list.pop()
        show_plate_list()


def welcome_message():
    global plate_list 
    command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

    Bienvenido al robot lavaplatos . ¿Qué deseas hacer?

    [A]gregar plato al lavabo
    [L]avar plato
    [M]ostrar platos
    '''))
    command.upper()
    if command == 'A':
        add_plate()
    elif command == 'L':
        wash_plate()
    elif command == 'M':    
        show_plate_list()
    else:
        print('Opción incorrecta')

    command_2 = str(input('¿Desea repetir el programa? \nYes\nNo\n '))
    command_2.upper()
    if command_2 == 'Y':
        welcome_message()

if __name__ == "__main__":
    welcome_message()

