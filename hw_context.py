from contextlib import contextmanager
from datetime import datetime

@contextmanager
def my_open(file_path):
    try:
        time_start = datetime.now()
        print('Время запуска кода в менеджере контекста:', time_start)
        file = open(file_path)
        yield file
    finally:
        file.close()
        time_finish = datetime.now()
        print('Время окончания работы кода:', time_finish)
        time_difference = time_finish - time_start
        print('На выполнение кода было потрачено:', time_difference)

with my_open('test_append.txt') as f: #как вставить encoding='utf-8', чтоб не было краказябр?
    def get_cook_book():
    #global cook_book
    #cook_book = {}
      for line in f:
        name_of_dish = line.strip()
        ingridient_count = f.readline()
        cook_book.setdefault(name_of_dish, list())
        for i in range(int(ingridient_count)):
          rec = f.readline().strip().split('|')
          ingredients = {'ingridient_name': rec[0], 'quantity': rec[1], 'measure': rec[2]}
          cook_book[name_of_dish].append(ingredients)
        f.readline()
      return cook_book

    cook_book = {}
    print(get_cook_book())

