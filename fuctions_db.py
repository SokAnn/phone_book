
# get list of users with telephones
def work_with_DB_users(curs, request):
    curs.execute(request)
    list_db = []
    for Name, Telephone, Bdate in curs:
        # print(f"Name: {Name}, \nTelephone: {Telephone}, \nDate: {Bdate}\n")
        list_db.append([Name, Telephone, Bdate])
    list_db.sort()
    return list_db

# get list of users with passwords
def work_with_DB_logins(curs, request):
    curs.execute(request)
    list_db = []
    for Name, Password, Bdate in curs:
        # print(f"Name: {Name}, \nTelephone: {Password}, \nDate: {Bdate}\n")
        list_db.append([Name, Password, Bdate])
    list_db.sort()
    return list_db