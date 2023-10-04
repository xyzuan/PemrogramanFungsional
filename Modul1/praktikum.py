# Sevenbook Python
db_user = {
    'admin': {
        'fullName': 'admin',
        'email': 'admin@xyzscape.xyz',
        'isAdmin': True
    },
    'xyzuan': {
        'fullName': 'Jody Yuantoro',
        'email': 'xyzuannihboss@gmail.com',
        'isAdmin': False
    },
    'nath': {
        'fullName': 'Geraldi Nathan',
        'email': 'nath@gmail.com',
        'isAdmin': False
    }
}

db_book = {
    1: {
        'title': 'Laskar Pelangi',
        'author': 'Jody Yuantoro',
        'category': 'Social',
        'available': True,
        'user': 'null'
    },
    2: {
        'title': 'Alhamdullilah Ya Allah',
        'author': 'Krisno',
        'category': 'Religi',
        'available': True,
        'user': 'null'
    },
}


def bookAdd():
    id = len(db_book) + 1
    title = input('Title: ')
    author = input('Author: ')
    category = input('Genre: ')
    db_book[id] = {
        'title': title,
        'author': author,
        'category': category,
        'available': True,
        'user': "null"
    }


def bookRead(data):
    for id, db, in db_book.items():
        print(f'-{id}------------')
        if db["available"] == False:
            if (data['isAdmin'] == True):
                print(f'Book loaned by {db["user"]}')
            else:
                print('Book not available')
        else:
            print('Book available to rent')
        print(
            f'Nama buku: {db["title"]}\nAuthor: {db["author"]}\nCategory: {db["category"]}\n')


def bookLoan(data):
    bookRead(data)
    userSelector = int(input('Select book id: '))
    if (db_book[userSelector]['available']):
        print('Book has been loaned')
        db_book[userSelector]['user'] = data['fullName']
        db_book[userSelector]['available'] = False
    else:
        print(f'The book have been loaned by {db_book[userSelector]["user"]}')


def bookReturn(data):
    for id, db, in db_book.items():
        if db["user"] == data["fullName"]:
            print(f'-{id}------------')
            print(
                f'Nama buku: {db["title"]}\nAuthor: {db["author"]}\nCategory: {db["category"]}\n')

    userSelector = int(input('Select book id: '))
    if (db_book[userSelector]['user'] == data['fullName']):
        print('Book has been returned')
        db_book[userSelector]['user'] = ''
        db_book[userSelector]['available'] = True
    else:
        print(f'The book not found')


def dashboard(data):
    while True:
        if data['isAdmin'] == True:
            print(f'Hello, {data["fullName"]}')
            print('1. Add book')
            print('2. List book')
            print('0. Log out')

            menuSelector = input('Select menu: ')
            match menuSelector:
                case '1':
                    bookAdd()
                case '2':
                    bookRead(data)
                case '0':
                    loginScreen()
                case default:
                    print('Command not available')
        else:
            print(f'Hello, {data["fullName"]}')
            print('1. Loan book')
            print('2. Return book')
            print('3. List book')
            print('0. Log out')

            menuSelector = input('Select menu: ')
            match menuSelector:
                case '1':
                    bookLoan(data)
                case '2':
                    bookReturn(data)
                case '3':
                    bookRead(data)
                case '0':
                    loginScreen()
                case default:
                    print('Command not available')


def loginScreen():
    while True:
        authUser = input("Input username: ")
        for userName, data, in db_user.items():
            if authUser == userName:
                dashboard(data)


if __name__ == "__main__":
    loginScreen()
