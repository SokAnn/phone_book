import datetime

# get list of users with telephones
def work_with_DB_users(curs, request):
    curs.execute(request)
    list_db = []
    for Name, Telephone, Bdate in curs:
        list_db.append([Name, Telephone, Bdate])
    list_db.sort()
    return list_db

# get list of users with passwords
def work_with_DB_logins(curs, request):
    curs.execute(request)
    list_db = []
    for Name, Password, Bdate in curs:
        list_db.append([Name, Password, Bdate])
    list_db.sort()
    return list_db

def formating_date(str_date):
    result = str_date[6:] + '-' + str_date[3:5] + '-' + str_date[0:2]
    return result

def get_BDate(users, now, week):
    res = []
    for i in range(len(users)):
        user = datetime.datetime.strptime(str(users[i][2]), "%Y-%m-%d")
        user = datetime.datetime(now.year, user.month, user.day)
        if (user >= now) and (user <= week):
            res.append(users[i][0])
    return res
