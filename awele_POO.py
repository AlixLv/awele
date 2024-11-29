class Player():
    def __init__(self, player_name):
        self.player_name = player_name
        self.__player_score = 0
        self.player_board = {}

    def get_player_name(self):
        return self.player_name   
    
    def get_player_board(self):
        return self.player_board

    def display_player_info(self):
        print(f"{self.player_name} has a score of {self.__player_score} points.")


class Game():
    def __init__(self, player1_name, player2_name):
        self.letters_to_display = " a  b  c  d  e  f  g  h  i  j  k  l "
        self.letters_to_dict = "abcdefghijkl"
        self.board = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        self.start_number_seeds = 48
        self.score = 0
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.current_player = self.player1
        self.index = 0


    def display_player_name(self):
        return f"{self.current_player.get_player_name()}"


    def display_number_of_seeds(self):
        print(f"Remaing seeds: {self.__start_number_seeds}")


    def display_board(self):
        length_board = len(self.board)
        middle_board = int(length_board / 2)
        self.first_part_board = self.board[:middle_board]
        self.second_part_board = self.board[middle_board:]
        self.second_part_board.reverse()

        length_letters = len(self.letters_to_display)
        middle_letters = int(length_letters / 2)
        self.first_part_letters = self.letters_to_display[:middle_letters]
        self.second_part_letters = self.letters_to_display[middle_letters:]
        self.second_part_letters = self.second_part_letters[::-1]

        print(self.second_part_letters)
        print(self.second_part_board)
        print(self.first_part_board)
        print(self.first_part_letters)

        return self.first_part_board, self.second_part_board

    # REFACTO A FAIRE player2_board_init et player1_board_init
    def player1_board_init(self):
        length_letters = len(self.letters_to_dict)
        middle_letters = int(length_letters / 2)
        self.first_part_letters_dict = self.letters_to_dict[:middle_letters]
        self.second_part_letters_dict = self.letters_to_dict[middle_letters:]

        self.player_board = self.player1.get_player_board()
        for key, value in zip(self.second_part_letters_dict, self.second_part_board):
            self.player_board[key] = value
        print(self.player_board)
        return self.player_board

    def player2_board_init(self):
        self.player_board = self.player2.get_player_board()
        for key, value in zip(self.first_part_letters_dict, self.first_part_board):
            self.player_board[key] = value
        print(self.player_board)
        return self.player_board


    def getting_user_index_for_saw(self):
        self.index = input("Sélectionnez le champs depuis lequel vous voulez semer: ")
        if self.current_player == self.player1 and self.index > "f" :
            self.index = input("Vous devez sélectionner un champ compris entre les lettres a et f incluses: ")
        elif self.current_player == self.player2 and self.index < "g":
            self.index = input("Vous devez sélectionner un champ compris entre les lettres g et l incluses: ")   
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
        

    def get_matching_index(self):
        self.index = "g"
        print(self.index)
        print(self.current_player.player_board)
        for key, value in self.current_player.player_board.items():
            print("IN FOR LOOP")
            print(key, "-", value)
            if self.index == key:
                print(key, value)
                self.index = value
                print("index: ", self.index, type(self.index))


    def get_next_index_harvest(self):
        if self.index == 0:
            return len(self.board) -1
        else:
            return self.index - 1


    def harvest(self):
        self.score = 0
        while self.board[self.index] >=2 and self.board[self.index] <= 3:
            self.score += self.board[self.index]
            self.board[self.index] = 0
            self.next_index = self.get_next_index_harvest()
            self.index = self.next_index
        self.start_number_seeds -= self.score 
        print(f"You're score: {self.score}")    


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
            awele.display_board()
            print(f"C'est au tour de {self.display_player_name()} de jouer")
            awele.getting_user_index_for_saw()
            awele.saw()
            awele.display_board()
            awele.getting_user_index_for_harvest()
            awele.harvest()
            if self.current_player == self.player1:
                self.current_player = self.player2
            else:
                self.current_player = self.player1    
 



awele = Game("Ada", "Audrey")
awele.start_turn()

    #TO DO 
    # fonction pour relier la lettre entrée dans input et l'index correspondant
    #en fonction du joueur en train de jouer, délimiter la partie du plateau à partir de laquelle il peut jouer
    #joueur1 = plateau[0] à plateau[5]
    #joueur2 = plateau[6] à plteau[11]