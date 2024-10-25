import pandas as pd

df = pd.read_csv('student_sleep_patterns.csv')


#print(df.head()) # по умолчанию выводит 5 строк сначала
#print(df.info()) # вывод информации о файле
print(df.describe())  #вывод статистической информации