import requests
print('Программа запустилась')
print('=== User API Manager ===')
def get_users():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users', timeout=5)
        response.raise_for_status()
        data = response.json()
        for user in data:
            print(user['id'],'-', user['name'],'-', user['email'])
    except requests.exceptions.RequestException as error:
        print('Ошибка:', error)
def get_user(user_id):
    try:
        response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}', timeout=5)
        response.raise_for_status()
        user = response.json()
        print('Имя:', user['name'])
        print('Email:', user['email'])
        print('Город:', user['address']['city'])
    except requests.exceptions.RequestException as error:
        print('Ошибка:', error)
def create_user(name, email):
    try:
        user = {
            'name' : name,
            'email' : email
        }
        response = requests.post('https://jsonplaceholder.typicode.com/users',json=user, timeout=5)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.RequestException as error:
        print('Ошибка:', error)
def delete_user(user_id):
    try:
        response = requests.delete(f'https://jsonplaceholder.typicode.com/users/{user_id}', timeout=5)
        response.raise_for_status()
        print('Пользователь удалён. Статус:',response.status_code)
    except requests.exceptions.RequestException as error:
        print('Ошибка:', error)
while True:
    print('1. Показать всех пользователей')
    print('2. Найти пользователя')
    print('3. Создать пользователя')
    print('4. Удалить пользователя')
    print('5. Выход')
    try:
        number = int(input('Введите число:'))
        if number == 1:
            get_users()
        elif number == 2:
            user_id = int(input('Введите id пользователя:'))
            get_user(user_id)
        elif number == 3:
            name = input('Введите имя пользователя:')
            email = input('Введите email:')
            create_user(name, email)
        elif number == 4:
            user_id = int(input('Введите id пользователя:'))
            delete_user(user_id)
        elif number == 5:
            break
        else:
            raise ValueError('Такого пункта нет в меню')
    except ValueError as error:
        print('Ошибка', error)



