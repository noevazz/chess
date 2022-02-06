import os

class Figure():
    def __init__(self, simbol: str, x: str, y: str):
        self.symbol = simbol
        self.__x = x
        self.__y = y
    
    def letter_to_num_for_vector_calc(self, letter: str):
        return ord(letter.lower())-97
    
    def num_for_vector_calc(self, num: int):
        return abs(8-num)

    def get_x_in_board(self):
        return ord(self.__x.lower())-97
    
    def get_y_in_board(self):
        return 8-int(self.__y)
    
    def set_x(self, x_value):
        self.__x = x_value
    
    def set_y(self, y_value):
        self.__y = y_value
    
    


class Horse(Figure):
    def __init__(self, simbol: str, x: str, y: str):
        super().__init__(simbol, x, y)
        #print(self.get_int_x(), self.get_int_y())
        # Magnitude of vector PQ, where P=(0,0) and Q=(2,1):
        #   No need to calculate |PR|, where R=(1,2),
        #   since the magnitude is the same as |PQ|
        self.__M_of_PQ = (2**2 + 1**2)**0.5
    
    def set_xy(self, x_value, y_value):
        new_x = (self.letter_to_num_for_vector_calc(x_value))
        new_y = (self.num_for_vector_calc(int(y_value)))
        current_x = (self.get_x_in_board())
        current_y = (self.get_y_in_board())
        #print(f"Current coordinates: {current_x},{current_y}")
        #print(f"New coordinates: {new_x},{new_y}")

        current_M = (current_x**2 + current_y**2)**0.5
        new_M = (new_x**2 + new_y**2)**0.5
        M = ((current_x-new_x)**2 + (current_y-new_y)**2)**0.5

        #print("M=", M, "M of PQ=", self.__M_of_PQ)
        #print("current_M=", current_M)
        #print("new_M=", new_M)
        #print()
        if M == self.__M_of_PQ:
            self.set_x(x_value)
            self.set_y(y_value)
        else:
            print("That's not a valid move for this horse")
            new_values = input("Enter valid values: ")
            self.set_xy(*new_values.split(','))

class Bishop(Figure):
    def __init__(self, simbol: str, x: str, y: str):
        super().__init__(simbol, x, y)
        #print(self.get_int_x(), self.get_int_y())
    
    def set_xy(self, x_value, y_value):
        self.set_x(x_value)
        self.set_y(y_value)


class Board:
    def draw_board(self, p1: Figure, p2: Figure):
        black = True
        fill = "\\"
        print("  ", "-"*10*8, "-", sep="")
        num = 8
        for base in range(8):
            black = not black
            for heigh in range(3):
                if heigh == 1:
                    print(num, end=" ")
                    num -= 1
                else:
                    print(" ", end=" ")

                for i in range(8):
                    fill = "\\" if black else " "
                    if base == p1.get_y_in_board() and heigh == 1 and i == p1.get_x_in_board():
                        print("|    " + p1.symbol + "    ", end="")
                    elif  base == p2.get_y_in_board() and heigh == 1 and i == p2.get_x_in_board():
                        print("|    " + p2.symbol + "    ", end="")
                    else:
                        print("|", fill*8, end="")
                    black = not black
                print("|")
            print("  ", "-"*10*8, "-", sep="")
        num_to_letter = 65
        print("  ", end="")
        for i in range(8):
            print(" "*5, chr(num_to_letter), " "*4, sep="", end="")
            num_to_letter += 1
        print()

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    board = Board()
    player1 = Horse('♞', 'B', '8')
    player2 = Bishop('♙', 'D', '1')
    board.draw_board(player1, player2)
    playing = True
    while playing:
        position_player1 = input(f"Enter nex position for player 1, example A,2: ")
        player1.set_xy(*position_player1.split(','))
        os.system('cls' if os.name == 'nt' else 'clear')
        board.draw_board(player1, player2)

        #position_player2= input(f"Enter nex position for player 2, example A,2: ")
        #player2.set_xy(*position_player2.split(','))
        #os.system('cls' if os.name == 'nt' else 'clear')
        #board.draw_board(player1, player2)
