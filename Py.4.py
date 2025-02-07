#AknurAiganym Қолданушының логині мен паролі
stored_login = "user123"
stored_password = "password123"

# Пайдаланушыдан логин мен пароль сұрау
login = input("Логинді енгізіңіз: ")
password = input("Парольді енгізіңіз: ")

# Логин мен парольді тексеру
if login == stored_login and password == stored_password:
    print("Қош келдіңіз!")
else:
    print("Қате логин немесе пароль!")
