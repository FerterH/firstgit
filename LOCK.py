password = 123
item = 0
miss = 0
activity = 0
secrets = ['жду нового человека паука', 'хочу каникулы', "кто прочитал тот молодец"]
wrpassword = 0
while True:
    wrpassword = input('Введите пароль')
    if  int(wrpassword) == password:
        print('Вы вошли в систему')
        break
    else:
        print("Пароль неверный")
        miss = miss + 1
        if miss == 3:
            while True:
                print('Система заблокирована')
print('Выберите действие')
print('1. Изменить пароль')
print('2. Вывести секретные данные')
print('3. Добавить секретные данные')
while True:
    activity = input()
    if int(activity) == 1:
        print('Введите новый пароль: ')
        password = input("")


    elif int(activity) == 2:
        print(secrets)


    elif int(activity) == 3:
        a = input("Введите новый секрет: ")
        secrets.append(a)












#print(secrets[2])