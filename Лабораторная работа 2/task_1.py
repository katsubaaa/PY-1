money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
valueOfMonth = 0
while money_capital >= 0:
    money_capital += salary
    money_capital -= spend
    spend = spend * (1 + increase)
    if money_capital >= 0:
        valueOfMonth += 1
print("Количество месяцев, которое можно протянуть без долгов:", valueOfMonth)
