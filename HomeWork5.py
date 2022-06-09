# 1. Напишите программу, удаляющую из текста все слова содержащие "абв". 
# Используйте знания с последней лекции. 
# Выполните ее в виде функции. 

# def abv_filter(str_text):
#     return ' '.join(filter(lambda s: 'абв' not in s, str_text.split()))

# print(abv_filter(input('Введите строку для проверки: ')))

# 2. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку. 

# from random import randint, choice

# "Выбираем уровень сложности"
# smart_level = 2  # Всего 3 уровня сложности: 0, 1, 2

# table = [[None for i in range(3)] for j in range(3)]
# empty_cells = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
# user_symb = 1  # у игрока крестики
# comp_symb = 0  # у компьютера нолики


# def print_table():
#     for r, row in enumerate(table):
#         for c, col in enumerate(row):
#             cell = table[r][c]
#             cell_char = '   ' if cell is None else ' X ' if cell else ' 0 '
#             end_char = '|' if c < 2 else '\n'
#             print(cell_char, end=end_char)
#         if r < 2:
#             print('---+---+---')

# def comp_thinking():
#     check_symb_list = [comp_symb, user_symb]
#     if smart_level:
#         for check_symb in check_symb_list[-smart_level:]:
#             for cell in empty_cells:
#                 x, y = map(int, cell)
#                 table[x - 1][y - 1] = check_symb
#                 if check_table() == check_symb:
#                     table[x - 1][y - 1] = None
#                     return cell
#                 table[x - 1][y - 1] = None
#     return choice(empty_cells)

# def step(is_player, symb):
#     if is_player:
#         coord_xy = '-'
#         while coord_xy not in empty_cells:
#             print('Возможные ходы', empty_cells)
#             print('Для завершения нажмите Enter')
#             coord_xy = input("Ваш ход (строка столбец без пробела): ")
#             if coord_xy == '':
#                 exit()
#     else:
#         coord_xy = comp_thinking()
#     empty_cells.remove(coord_xy)
#     x, y = map(int, coord_xy)
#     table[x - 1][y - 1] = symb
#     if not is_player:
#         print(f'Ход компьютера ({x}, {y})')


# def check_table():
#     "Проверка есть ли выигрыш"
#     # проходим по строкам
#     for i in table:
#         if i[0] is not None and i[0] == i[1] == i[2]:
#             return i[0]
#     # проходим по столбцам
#     for j in range(3):
#         col = [i[j] for i in table]
#         if col[0] is not None and col[0] == col[1] == col[2]:
#             return col[0]
#     # проверяем диагонали
#     if table[0][0] is not None and table[0][0] == table[1][1] == table[2][2]:
#         return table[0][0]
#     if table[2][0] is not None and table[2][0] == table[1][1] == table[0][2]:
#         return table[2][0]
#     # проверяем заполнена ли таблица
#     for item in table:
#         if list(filter(lambda i: i is None, item)) != []:
#             break
#     else:
#         return 'ничья'
#     return None


# def play_game():
#     check = None
#     turn_X = True  # показывает чей ход
#     # Основной цикл игры
#     # Игра идет пока функция chek не вернет результат отличный от None
#     while check is None:
#         step(turn_X, user_symb if turn_X else comp_symb)
#         if not turn_X:
#             print_table()
#         check = check_table()
#         turn_X = not turn_X
#     if check is not None:
#         if check == user_symb:
#             print_table()
#             print("Поздравляю, вы победили!!")
#         elif check == comp_symb:
#             print("Победил компьютер")
#         else:
#             print("Ничья!")


# if __name__ == '__main__':
#     play_game()

# 3.  Вот вам текст:
# «Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин.
# Ну, эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем,
# по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда.
# Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают.
# Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче.
# Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо.
# Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой
# и не упал в эту… ээээ… яму. Хлеба купил».

# Отфильтруйте его, чтобы эту фигню можно было прочесть. 
# Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.

def filter_text(file_path: str) -> None:
    filler_words = [',', 'короче говоря', 'короче', 'кстати', 'эээээ', 'ээээ', 'эээ', 'кажется', 'ясен пень', 'в общем', 'ну', 'как бы']

    with open(file_path, "r", encoding='utf-8') as file:
        test_line = file.readline().lower()
        print(test_line)
        for filler_word in filler_words:
            test_line = test_line.replace(', ' + filler_word, '')
        for filler_word in filler_words:
            test_line = test_line.replace(' ' + filler_word, '')
        for filler_word in filler_words:
            test_line = test_line.replace(filler_word, '')

    while test_line[1] == ',' or test_line[1] == ' ' or test_line[1] == '...':
        test_line = test_line[1:]

    test_line = '«' + test_line

    with open(file_path, "w", encoding='utf-8') as file:
        file.write(test_line)


filter_text('text.txt')

# 4. Чисто для тренировки новый функций, ничего сложного. Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого плюс 1. Вам нужно сделать две функции: первая из которых 
# создаст список кортежей, состоящих из номера и языка, написанного большими буквами. Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, 
# то кортеж остается, его номер заменяется на сумму очков. Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем 
# столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы. С помощью reduce сложите получившиеся числа и верните из функции в качестве ответа.

