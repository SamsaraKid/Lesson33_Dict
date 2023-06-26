import random
import time

sword = {'name': 'Меч', 'material': 'bronze', 'min': 10, 'max': 12}
stone = {'name': 'Камень', 'material': 'stone', 'min': 7, 'max': 15}
batarang = {'name': 'Бэтаранг', 'material': 'metal', 'min': 6, 'max': 16}
friendship = {'name': 'Дружба', 'material': 'magic', 'min': 9, 'max': 13}
family = {'name': 'Семья', 'material': 'people', 'min': 8, 'max': 14}


warrior1 = {'name': 'Boris', 'nick': 'Britva', 'hp': 100, 'weapon': sword}
warrior2 = {'name': 'Bob', 'nick': 'Gubka', 'hp': 100, 'weapon': stone}
warrior3 = {'name': 'Bruce', 'nick': 'Batman', 'hp': 100, 'weapon': batarang}
warrior4 = {'name': 'Pony', 'nick': 'Pinky Pie', 'hp': 100, 'weapon': friendship}
warrior5 = {'name': 'Torreto', 'nick': 'Dom', 'hp': 100, 'weapon': family}

warriors = [warrior1, warrior2, warrior3, warrior4, warrior5]




weapons = [sword, stone, batarang, friendship, family]



def battle(b1, b2):
    print('На арену выходят!')
    print(b1['name'], b1['nick'], 'с оружием', b1['weapon']['name'])
    print(b2['name'], b2['nick'], 'с оружием', b2['weapon']['name'])
    print('Начинаем поединок!')
    while b1['hp'] > 0 and b2['hp'] > 0:
        udar(b1, b2)
        if b2['hp'] <= 0:
            break
        else:
            udar(b2, b1)
    time.sleep(1)
    if b2['hp'] <= 0:
        print('У нас победитель!')
        print(b1['name'], b1['nick'])
    elif b1['hp'] <= 0:
        print('У нас победитель!')
        print(b2['name'], b2['nick'])


def udar(b1, b2):
    # time.sleep(1)
    r = random.randint(b1['weapon']['min'], b1['weapon']['max'])
    print(b1['name'], 'ударил на', r)
    b2['hp'] -= r
    print('У', b2['name'], 'осталось здоровья', b2['hp'])



print('Выберите воинов:')
for w in range(len(warriors)):
    print(w + 1, '-', warriors[w]['name'], warriors[w]['nick'])

i1 = int(input('Первый воин:\n'))

print('Выберите его оружие:')
for w in range(len(weapons)):
    print(w + 1, '-', weapons[w]['name'])
w1 = int(input())
warriors[i1 - 1]['weapon'] = weapons[w1 - 1]

i2 = int(input('Второй воин:\n'))

print('Выберите его оружие:')
for w in range(len(weapons)):
    print(w + 1, '-', weapons[w]['name'])
w2 = int(input())
warriors[i2 - 1]['weapon'] = weapons[w2 - 1]

battle(warriors[i1 - 1], warriors[i2 - 1])


