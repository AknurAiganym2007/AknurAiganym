#AknurAiganym Пайдаланушыдан сан сұрау
num = input("Санды енгізіңіз: ")

# Цифрлар саны
num_length = len(num)

# Цифрлар қосындысы
digit_sum = sum(int(digit) for digit in num)

# Палиндромды тексеру
is_palindrome = num == num[::-1]

# Нәтижелерді шығару
print(f"Цифрлар саны: {num_length}")
print(f"Цифрлар қосындысы: {digit_sum}")
if is_palindrome:
    print("Бұл сан палиндром.")
else:
    print("Бұл сан палиндром емес.")
