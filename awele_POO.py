class Player():
    def __init__(self, player_name):
        self.player_name = player_name
        self.__player_score = 0

    def get_player_name(self):
        return self.player_name   

    def display_player_info(self):
        print(f"{self.player_name} has a score of {self.__player_score} points.")


class Game():
    def __init__(self, player1_name, player2_name):
        self.letters = " a  b  c  d  e  f g  h  i  j  k  l"
        self.board = [4,4,4,4,2,2,3,2,4,4,4,4]
        self.start_number_seeds = 48
        self.score = 0
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.current_player = self.player1
        self.index = 7

    def display_player_name(self):
        return f"{self.current_player.get_player_name()}"

    def display_number_of_seeds(self):
        print(f"Remaing seeds: {self.__start_number_seeds}")

    def display_board(self):
        length_board = len(self.board)
        middle_board = int(length_board / 2)
        first_part_board = self.board[:middle_board]
        second_part_board = self.board[middle_board:]
        second_part_board.reverse()

        length_letters = len(self.letters)
        middle_letters = int(length_letters / 2)
        first_part_letters = self.letters[:middle_letters]
        second_part_letters = self.letters[middle_letters:]
        second_part_board.reverse()

        print(second_part_letters)
        print(second_part_board)
        print(first_part_board)
        print(first_part_letters)

    def getting_user_index_for_saw(self):
        self.index = input("Sélectionnez le champs depuis lequel vous voulez semer: ")
        self.index = int(self.index)
        return self.index
    
    def getting_user_index_for_harvest(self):
        self.index = input("Sélectionnez le champs à partir duquel vous voulez récoltez: ")
        self.index = int(self.index)
        return self.index
    
    def get_next_index_saw(self):
        if self.index == len(self.board) -1:
            return 0
        else:
            return self.index +1

    def get_next_index_harvest(self):
        if self.index == 0:
            return len(self.board) -1
        else:
            return self.index - 1

    def harvest(self):
        self.score = 0
        print("board[index]: ", self.board[self.index])
        while self.board[self.index] >=2 and self.board[self.index] <= 3:
            print("IN WHILE LOOP")
            self.score += self.board[self.index]
            print("score: ", self.score)
            self.board[self.index] = 0
            print("board: ", self.board)
            self.next_index = self.get_next_index_harvest()
            print("next index: ", self.next_index)
            self.index = self.next_index
            print("index: ", self.index)
        self.start_number_seeds -= self.score 
        print("start number of seeds: ", self.start_number_seeds)
        print(f"You're score: {self.score}")    

    #TO DO 
    #en fonction du joueur en train de jouer, délimiter la partie du plateau à partir de laquelle il peut jouer
    #joueur1 = plateau[0] à plateau[5]
    #joueur2 = plateau[6] à plteau[11]
    def saw(self):
        self.number_of_seeds = self.board[self.index]
        self.board[self.index] = 0
        self.next_index = 0

        while self.number_of_seeds > 0:
            self.next_index = self.get_next_index_saw()
            self.board[self.next_index] +=1
            self.number_of_seeds -= 1
            self.index = self.next_index  



    def start_turn(self):
        while self.start_number_seeds > 0:
            # print("Le plateau de départ : [3, 4, 3, 2, 7, 8, 7, 3, 3, 7, 5, 3]")
            awele.display_board()
            print(f"C'est au joueur {self.display_player_name()} de jouer")
            # print("Un input pour demander sur quelle case joueur commence: [index]")
            awele.getting_user_index_for_saw()
            # print("on récupère [index] et on exécute saw(index)")
            awele.saw()
            awele.display_board()
            # print("Input : demande au joueur à partir de quelle case iel veut ramasser graines: [index]")
            awele.getting_user_index_for_harvest()
            # print("on appelle harvest(index)")
            awele.harvest()
            if self.current_player == self.player1:
                self.current_player = self.player2
            else:
                self.current_player = self.player1    
 



awele = Game("Ada", "Audrey")
awele.start_turn()

