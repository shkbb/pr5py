def check_cooling_system():
    try:
        temperature = float(input("Введіть температуру (°C): "))
        humidity = float(input("Введіть відносну вологість (%): "))
        
        if temperature > 30 and humidity > 70:
            print("Активація системи охолодження")
        else:
            print("Умови нормальні")
    except ValueError:
        print("Помилка вводу! Будь ласка, введіть числові значення.")


def validate_input():
    try:
        number = int(input("Введіть число (1-100): "))
        
        if 1 <= number <= 100:
            print("Число знаходиться в межах від 1 до 100.")
        else:
            print("Число виходить за межі допустимого діапазону.")
    except ValueError:
        print("Помилка вводу! Введіть ціле число.")


def candidate_selection():
    try:
        age = int(input("Введіть вік кандидата: "))
        experience = int(input("Введіть кількість років досвіду: "))
        qualification = input("Чи має кандидат спеціальну кваліфікацію? (True/False): ").strip().lower()
        
        if qualification == "true":
            qualification = True
        elif qualification == "false":
            qualification = False
        else:
            print("Помилка вводу! Введіть 'True' або 'False'.")
            return
        
        if 25 <= age <= 50 and (experience >= 3 or qualification):
            print("Кандидат відповідає вимогам")
        else:
            print("Кандидат не відповідає вимогам")
    except ValueError:
        print("Помилка вводу! Введіть коректні числові значення.")


def main():
    print("Оберіть завдання:")
    print("1 - Перевірка критичних умов")
    print("2 - Валідація введення користувача")
    print("3 - Відбір кандидатів")
    
    choice = input("Введіть номер завдання (1-3): ")
    
    if choice == "1":
        check_cooling_system()
    elif choice == "2":
        validate_input()
    elif choice == "3":
        candidate_selection()
    else:
        print("Помилка вибору! Введіть число від 1 до 3.")


if __name__ == "__main__":
    main()
