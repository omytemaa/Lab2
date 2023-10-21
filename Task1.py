money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0
while money_capital > 0:
    if months >0:
        spend *= (1 + increase)
    money_capital = money_capital + salary - spend
    if money_capital >=0:
        months += 1
print("Количество месяцев, которое можно протянуть без долгов:", months)
