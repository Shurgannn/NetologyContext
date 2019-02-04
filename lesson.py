from contextlib import contextmanager
from datetime import datetime

@contextmanager
def time():
    time1 = f'{str(datetime.now())}\n'
    print('Время запуска кода в менеджере контекста', time1)
    yield

with(time()):
    time2 = f'{str(datetime.now())}\n'
    print('Время окончания работы кода', time2)




      #file1.write(now)
      #print('Время окончания работы кода:', datetime.now())
      #print(file.read())