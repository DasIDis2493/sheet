"""
Срвнение типов
"""

if __name__ == "__main__":
    VAULE_1 = input("Первое значение:")
    VAULE_2 = input("Второе значение:")
    try:
        RESULT = int(VAULE_1) + int(VAULE_2)
    except ValueError:
        RESULT = VAULE_1 + VAULE_2

    print(RESULT)
