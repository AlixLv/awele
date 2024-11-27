board = [1, 0, 3, 0, 0, 5, 6, 0, 0, 7, 0, 3]

def main():
    print("DISPLAY BOARD: ")
    display_board(board) 
    saw(6)
    print("DISPLAY BOARD AFTER SAW: ")
    display_board(board) 
    # harvest(6)
    # print("DISPLAY BOARD AFTER HARVEST: ")
    # display_board(board) 

def display_board(list):
    length = len(list)
    middle = int(length / 2)
    first_part = list[:middle]
    second_part = list[middle:]
    second_part.reverse()
    print(second_part)
    print(first_part)
    

def saw(index):
    number_of_seeds = board[index]

    board[index] = 0

    current_index = index
    print("CURRENT INDEX AT START: ", current_index)

    while number_of_seeds > 0:
        current_index = get_next_index_saw(current_index)
        print("CURRENT_INDEX: ", current_index)
        board[current_index] += 1
        number_of_seeds -= 1

        # TO DO 
        # ni = get next index clockwise 
        # board[ni] ++

def harvest(index):
    # TO DO
    # ajouter en paramètre le joueur qui récolte
    score = 0
    next_index = index

    # on peut ramasser uniquement s'il y a plus de 2 graines dans la case
    while board[next_index] >= 2:
        score += board[next_index]
        board[next_index] = 0
        next_index = get_next_index_harvest(next_index)
        # si l'index change de ligne, on break pour que le joueur évite de ramasser ses propres graines
        if next_index <= 5:
            break

    print("score : ", score)


def get_next_index_saw(index):
    if index == len(board):
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