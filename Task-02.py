# Задача 2. Поиск файла 2

import os
import random

def file_search(path, file, path_list):
    for element in os.listdir(path):
        fullpath = os.path.join(path, element)
        if element == file:
            path_list.append(fullpath)
        if os.path.isdir(fullpath):
            file_search(fullpath, file, path_list)


user_path = input("Введите путь поиска: ")
user_file = input("Введите файл, который нужно найти: ")

user_list = list()
file_search(user_path, user_file, user_list)
for element in user_list:
    print(element)
print(f"\nНайдено {len(user_list)} объектов.\n")

if len(user_list):
    random_object = random.choice(user_list)
    print("Показываю содержимое случайного объекта")
    print("Выбран объект:", random_object)
    user_file = open(random_object, 'r', encoding='utf-8')
    print("\nСодержимое файла:\n")
    for line in user_file:
        print(line, end='')

