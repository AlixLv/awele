board = [3, 4, 3, 2, 7, 8, 7, 3, 3, 7, 5, 3]

def main():
    print("DISPLAY BOARD: ")
    display_board(board) 
    saw(6)
    print("DISPLAY BOARD 🌱: ")
    display_board(board) 
    harvest(9)
    print("DISPLAY BOARD ♻️: ")
    display_board(board) 

def display_board(list):
    length = len(list)
    middle = int(length / 2)
    first_part = list[:middle]
    second_part = list[middle:]
    second_part.reverse()
    print(second_part)
    print(first_part)
    

def saw(index):
    #TO DO
    #en fonction du joueur en train de jouer, délimiter la partie du plateau à partir de laquelle il peut jouer
    #joueur1 = plateau[0] à plateau[5]
    #joueur2 = plateau[6] à plteau[11]
    number_of_seeds = board[index]
    board[index] = 0
    
    while number_of_seeds > 0:
        next_index = get_next_index_saw(index)
        board[next_index] += 1
        number_of_seeds -= 1
        index = next_index
    

def harvest(index):
    # TO DO
    # ajouter paramètre du joueur pour gérer le score
    score = 0
    # on peut ramasser uniquement s'il y a plus de 2 graines dans la case
    while board[index] >= 2:
        score += board[index]
        board[index] = 0
        next_index = get_next_index_harvest(index)
        index = next_index
    print(f"You're score: {score}")


def get_next_index_saw(index):
    if index == len(board)-1:
        return 0
    else:
        return index + 1


def get_next_index_harvest(index):
    # return (len(board) - 1 - ((index + 1) % len(board)))
    if index == 0:
        return len(board)-1
    else:
        return index - 1

main()