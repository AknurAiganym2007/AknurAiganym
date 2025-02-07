#AknurAiganym Пайдаланушыдан жылды енгізуді сұрау
year = int(input("Жылды енгізіңіз: "))

# Кібісе жылды анықтау
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} жылы кібісе жыл.")
else:
    print(f"{year} жылы кәдімгі жыл.")
