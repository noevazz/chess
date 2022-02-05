import os

class Figure():
    def __init__(self, simbol: str, x: str, y: str):
        self.symbol = simbol
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return ord(self.__x.lower())-97
    
    @x.setter
    def x(self, x_value):
        self.__x = x_value

    @property
    def y(self):
        return 8-int(self.__y)
    
    @y.setter
    def y(self, y_value):
        self.__y = y_value

        

class Horse(Figure):
    def __init__(self, simbol: str, x: str, y: str):
        super().__init__(simbol, x, y)
        #print(self.get_int_x(), self.get_int_y())

class Bishop(Figure):
    def __init__(self, simbol: str, x: str, y: str):
        super().__init__(simbol, x, y)
        #print(self.get_int_x(), self.get_int_y())


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
                    if base == p1.y and heigh == 1 and i == p1.x:
                        print("|    " + p1.symbol + "    ", end="")
                    elif  base == p2.y and heigh == 1 and i == p2.x:
                        print("|    " + p2.symbol + "    ", end="")
                    else:
                        print("|", fill*8, end="")
                    black = not black
                print("|")
            print("  ", "-"*10*8, "-", sep="")
        num_to_letter = 65
        for i in range(8):
            print(" "*5, chr(num_to_letter), " "*4, sep="", end="")
            num_to_letter += 1
        print()

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    board = Board()
    player1 = Horse('♞', 'A', '7')
    player2 = Bishop('♙', 'B', '6')
    board.draw_board(player1, player2)
    playing = True
    while playing:
        position_player1 = input(f"Enter nex position for player 1, example A,2: ")
        print(position_player1.split(','))
        player1.x, player1.y = position_player1.split(',')
        print(player1.x, player1.y)
        os.system('cls' if os.name == 'nt' else 'clear')
        board.draw_board(player1, player2)

        position_player2= input(f"Enter nex position for player 2, example A,2: ")
        player2.x, player2.y = position_player2.split(',')
        print(player1.x, player1.y)
        os.system('cls' if os.name == 'nt' else 'clear')
        board.draw_board(player1, player2)
