import random 


EMPTY = ' '

CHAIR1 = 'Стул1'

CHAIR2 = 'Стул2'

ARMCHAIR = 'Кресло'

TABLE = 'Стол'

CLOSET = 'Шкаф'

STOP_WORD = 'stop'

WELCOME = "Добро пожаловать в игру 'Расстановка мебели'"

OUT = 'Пока!'

RULES = '''Вводите номер клетки, с которой вы хотите передвинуть предмет на пустую клетку.' 
'Задача - поменять местами кресло и шкаф
*для экстренного выхода напиши: stop
'''

WIN_WORDS = 'Прекрасно! Вы победили!'


def main():
    welcome()
    logic(init_coordinates())


def welcome():
    print(WELCOME, RULES, sep='\n')


def logic(start_coordinates):
    coordinates = start_coordinates.copy()
    while True:
        item , out_word = get_item(coordinates)
        if out_word == True:
            out_game()
            break
        elif check_win(start_coordinates, move(item, coordinates)):
            win(coordinates)
            break


def init_coordinates():
    coordinates = {}
    items = {CHAIR1, CHAIR2, ARMCHAIR, TABLE, CLOSET, EMPTY}
    temp = set()
    for i in range(6):
        while True:
            n = random.randrange(1, 7)
            if n not in temp:
                temp.update({n})
                break
        coordinates[n] = items.pop()
    return coordinates 


def get_item(coordinates):
    while True:
        graphics(coordinates)
        print('Какой предмет будете передвигать?\n...')
        number = input('Введите номер клетки: ')
        out = check_out(number)
        if out == True:
            break
        elif number in '123456' and len(number) == 1:
            if ckeck_move(int(number), coordinates):
                break
            else:
                print('...\nДанный ход невозможен\n...')  
        else:
            print('...\nНет такой клетки...')   
    return number, out
    
def check_out(out_word):
    if out_word.lower() == STOP_WORD:
        if input('Вы хотите выйти? y/n : ') == 'y':
            return True  


def ckeck_move(number, coordinates):
    for key, value in coordinates.items():
        if value == EMPTY:
            num_empty = key
            break
    if abs(num_empty - number) == 3 or abs(num_empty - number) == 1:
        if (num_empty == 4 and number == 3) or (num_empty == 3 and number == 4):
            return False
        return True


def move(number, coordinates):
    item = coordinates[int(number)]
    for key, value in coordinates.items():
        if value == EMPTY:
            x = key
            break
    coordinates[x] = item
    coordinates[int(number)] = EMPTY
    return coordinates 
   

def check_win(start_coordinates, coordinates):
    for key, value in start_coordinates.items():
        if value == ARMCHAIR:
            item1 = coordinates[key]
        elif value == CLOSET:
            item2 = coordinates[key]
    return item2 == ARMCHAIR and item1 == CLOSET

   
def win(coordinates):
    graphics(coordinates)
    print(WIN_WORDS)


def out_game():
    print(OUT)


def graphics(coordinates):
    c = coordinates
    max_width = max(len(value) for value in c.values())
    sep = "+" + ("-" * (max_width + 6) + "+") * 3
    line1 = f'| 1 | {c[1]}{" "*(max_width - len(c[1]))} | 2 | {c[2]}{" "*(max_width - len(c[2]))} | 3 | {c[3]}{" "*(max_width - len(c[3]))} |'
    line2 = f'| 4 | {c[4]}{" "*(max_width - len(c[4]))} | 5 | {c[5]}{" "*(max_width - len(c[5]))} | 6 | {c[6]}{" "*(max_width - len(c[6]))} |'
    field = [sep, line1, sep, line2, sep]
    print(*field,sep='\n')

main()


    