#AknurAiganym Пайдаланушыдан бастапқы салым сомасын, жыл санын және жылдық пайыздық мөлшерлемені сұрау
initial_deposit = float(input("Бастапқы салым сомасын енгізіңіз: "))
years = int(input("Жылдар санын енгізіңіз: "))
interest_rate = float(input("Жылдық пайыздық мөлшерлемені енгізіңіз (мысалы, 5 үшін 5): "))

# Депозиттің әр жылдағы сомасын есептеу
deposit = initial_deposit
for year in range(1, years + 1):
    deposit += deposit * (interest_rate / 100)  # Өсім қосу
    print(f"{year}-шы жыл: {deposit:.2f} теңге")

