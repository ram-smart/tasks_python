def calculation_income(rate, money, month):
    if money <= 0:
        return 0
    for i in range(1, month + 1):
        money = round(money + money * rate / 100 / 12, 2)
        return money


def main():
    rate = 10
    money = 100000
    month = 12

    result = calculation_income(rate, money, month)
    print("Параметры счета:" "\n",
          "Сумма: ", money, "\n",
          "Ставка: ", rate, "\n",
          "Период: ", month, "\n",
          "Сумма на счете конце периода: ", result)


if __name__== "__main__":
    main()