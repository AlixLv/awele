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
        self.board = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        self.start_number_seeds = 48
        self.score = 0
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.current_player = self.player1

    def display_player_name(self):
        return f"{self.current_player.get_player_name()}"

    def display_number_of_seeds(self):
        print(f"Remaing seeds: {self.__start_number_seeds}")

    def display_board(self):
        length = len(self.board)
        middle = int(length / 2)
        first_part = self.board[:middle]
        second_part = self.board[middle:]
        second_part.reverse()
        print(second_part)
        print(first_part)

    def getting_user_index_for_saw(self):
        self.index = input("Sélectionnez le champs depuis lequel vous voulez semer: ")
        self.index = int(self.index)
        return self.index
    
    #TO DO REVOIR SAW et GET NEXT INDEX SAW
    def saw(self):
        self.number_of_seeds = self.board[self.index]
        self.board[self.index] = 0
        self.next_index = 0

        while self.number_of_seeds > 0:
            self.next_index = self.next_index.get_next_index_saw(self.index)
            self.board[self.next_index] +=1
            self.number_of_seeds -= 1
            self.index = self.next_index    

    def get_next_index_saw(self):
        if self.index == len(self.board) -1:
            return 0
        else:
            return self.index +1

    def start_turn(self):
        while self.__start_number_seeds > 0:
            print("Le plateau de départ : [3, 4, 3, 2, 7, 8, 7, 3, 3, 7, 5, 3]")
            print(f"C'est au joueur {self.display_player_name()} de jouer")
            print("Un input pour demander sur quelle case joueur commence: [index]")
            print("on récupère [index] et on exécute saw(index)")
            print("Input : demande au joueur à partir de quelle case iel veut ramasser graines: [index]")
            print("on appelle harvest(index)")
            self.__start_number_seeds -= 4
            self.display_number_of_seeds() 
            if self.current_player == self.player1:
                self.current_player = self.player2
            else:
                self.current_player = self.player1    
 




awele = Game("Ada", "Audrey")
# awele.start_turn()
awele.display_board()
awele.getting_user_index_for_saw()
awele.saw()

#TO DO
#AJOUTER LETTRES POUR QUE USER PUISSE SELECTIONNER UN CHAMPS

#def saw
#en fonction du joueur en train de jouer, délimiter la partie du plateau à partir de laquelle il peut jouer
#joueur1 = plateau[0] à plateau[5]
#joueur2 = plateau[6] à plteau[11]