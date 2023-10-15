users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
Users = \
    {
        "Общее количество": 0,
        "Уникальные посещения": 0
    }
SizeOfUsers = len(users)
AmountOfUnique = len(set(users))

Users["Общее количество"] = SizeOfUsers
Users["Уникальные посещения"] = AmountOfUnique


print(Users)