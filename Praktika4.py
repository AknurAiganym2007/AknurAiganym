# Функция шахмат атын тексеру үшін
def is_knight_move_valid(start, end):
    # Бастапқы және соңғы координаталарды бөлшектеу
    start_col, start_row = start[0], int(start[1])
    end_col, end_row = end[0], int(end[1])
    
    # Әріптерді санға түрлендіру
    start_col = ord(start_col) - ord('a')
    end_col = ord(end_col) - ord('a')

    # Аттың жүрісі шартын тексеру
    col_diff = abs(start_col - end_col)
    row_diff = abs(start_row - end_row)

    # Аттың жүрісі "L" пішінімен болуы керек (бір бағытта 2 алаң, екінші бағытта 1 алаң)
    if (col_diff == 2 and row_diff == 1) or (col_diff == 1 and row_diff == 2):
        return True
    else:
        return False

# Пайдаланушыдан бастапқы және соңғы координаталарды сұрау
start_pos = input("Бастапқы координатаны енгізіңіз (мысалы, a1): ")
end_pos = input("Соңғы координатаны енгізіңіз (мысалы, h8): ")

# Тексеру
if is_knight_move_valid(start_pos, end_pos):
    print("Ат дұрыс жүре алады.")
else:
    print("Ат дұрыс жүре алмайды.")
