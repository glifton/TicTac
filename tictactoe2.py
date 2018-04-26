import os

def choose_char():
	chosen = False
	while chosen == False:
		player_one = input("You will play Tic Tac Toe\nWho goes first? X or O: \n")
		if player_one.upper() == "X":
			print("Player 1 is X\nPlayer 2 is O")
			Players.append("X")
			Players.append("O")
			chosen = True
		elif player_one.upper() == "O" or player_one == "0":
			print("Player 1 is O\nPlayer 2 is X")
			Players.append("O")
			Players.append("X")
			chosen = True
		else:
			print("You haven't chosen a proper character")
			chosen = False
	return Players

def tictacboard():
	print("      |       |")
	print(f"   {Bloc[2][0]}  |   {Bloc[2][1]}   |   {Bloc[2][2]}")
	print("______|_______|______")
	print("      |       |")
	print(f"   {Bloc[1][0]}  |   {Bloc[1][1]}   |   {Bloc[1][2]}")
	print("______|_______|______")
	print("      |       |")
	print(f"   {Bloc[0][0]}  |   {Bloc[0][1]}   |   {Bloc[0][2]}")
	print("      |       |")

os.system('cls')
Bloc = [['1','2','3'],['4','5','6'],['7','8','9']]
KeepPlay = True
Players = []	#Players
xPlay = []
yPlay = []
Pturn = 0	#Player's Turn
OpenSpots = 9
print("Tic Tac Toe Game Time!\n\n")
tictacboard()
choose_char()
Bloc = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


def WinnerCheck(rows,players):
	if (Bloc[rows][0] == Bloc[rows][1] == Bloc[rows][2]):
		print(f"Player {players} is the winner!")
		return False
	elif (Bloc[0][0] == Bloc[1][0] == Bloc[2][0] != " ") or (Bloc[0][1] == Bloc[1][1] == Bloc[2][1] != " ") or (Bloc[0][2] == Bloc[1][2] == Bloc[2][2] != " "):
		print(f"Player {players} is the winner!")
		return False
	elif (Bloc[0][0] == Bloc[1][1] == Bloc[2][2] != " ") or (Bloc[2][0] == Bloc[1][1] == Bloc[0][2] != " "):
		print(f"Player {players} is the winner!")
		return False
	else:
		return True


while KeepPlay == True:
	choose_spot = int(input(f"\nPlayer {Players[Pturn]}'s turn "))
	if choose_spot-1 in range(0,3):
		if Bloc[0][choose_spot-1] == " ":
			os.system('cls')
			Bloc[0][choose_spot-1] = Players[Pturn]			
			if WinnerCheck(0,Players[Pturn]) == False:
				break			
			Pturn += 1
			tictacboard()
			OpenSpots += -1
		if Pturn == 2:
			Pturn = 0
			continue
		if OpenSpots == 0:
			KeepPlay = False	
	elif choose_spot-1 in range(3,6):
		if Bloc[1][choose_spot-4] == " ":
			os.system('cls')
			Bloc[1][choose_spot-4] = Players[Pturn]			
			if WinnerCheck(1,Players[Pturn]) == False:
				break
			Pturn += 1
			tictacboard()
			OpenSpots += -1
		if Pturn == 2:
			Pturn = 0
			continue
		if OpenSpots == 0:
			KeepPlay = False
	elif choose_spot-1 in range(6,9):
		if Bloc[2][choose_spot-7] == " ":
			os.system('cls')
			Bloc[2][choose_spot-7] = Players[Pturn]
			if WinnerCheck(2,Players[Pturn]) == False:
				break
			Pturn += 1
			tictacboard()
			OpenSpots += -1
		if Pturn == 2:
			Pturn = 0
			continue
		if OpenSpots == 0:
			os.system('cls')
			print("No winner this time, try again!".title())
			KeepPlay = False
	else:
		os.system('cls')
		tictacboard()
		print("Invalid Selection, choose again")
		continue

tictacboard()
print("Thanks For Playing!")