#!Программа Банковский счет
import account

def main():
    rate = int(input("Введите процентную ставку"))
    money = int(input("Введите сумму"))
    month = int(input("Введите период ведения счета в месяцах"))

    result = account.calculation_income(rate, money, month)
    print("Параметры счета:" "\n",
          "Сумма: ", money, "\n",
          "Ставка: ", rate, "\n",
          "Период: ", month, "\n",
          "Сумма на счете конце периода: ", result)

if __name__ == "__main__":
    main()