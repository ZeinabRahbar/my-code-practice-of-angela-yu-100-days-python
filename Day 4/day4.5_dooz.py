row1 = [".", ".", "."]
row2 = [".", ".", "."]
row3 = [".", ".", "."]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where you put the treasure??? ")

raw = int(position[0]) 
col = int(position[1])

selected_raw = map[raw - 1]
selected_raw[col - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")


