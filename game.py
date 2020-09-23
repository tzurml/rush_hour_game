class Game:
    """
    a class that run a rush_hour game, it getting a board and let the user
    an option to move the cars on the board
    """

    ERR_INPUT_MASSAGE = "\nNot a valid input\n"
    WIN_MSG = "\nYOU WON!!!\n"

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.__game_over = False
        self.__board = board

    def __single_turn(self):
        """
        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.
        """

        board = self.__board
        print(board)
        while True:
            user_input = input().split(',')
            if len(user_input) != 2:
                print(Game.ERR_INPUT_MASSAGE)
                continue
            else:
                name = user_input[0]
                movekey = user_input[1]
                if board.move_car(name, movekey):
                    if board.cell_content(board.target_location()):
                        self.__game_over = True
                    return True
                else:
                    print(Game.ERR_INPUT_MASSAGE)

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """

        # implement your code here (and then delete the next line - 'pass')
        while not self.__game_over :
            self.__single_turn()
        print(Game.WIN_MSG)
        return


if __name__ == "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section.
    from helper import load_json
    import sys
    from car import Car
    from board import Board

    VALID_CAR_NAME = ['Y', 'B', 'O', 'W', 'G', 'R']
    MIN_LENGTH = 2
    MAX_LENGTH = 4
    VALID_ORIENTATION = [0, 1]

    filename = sys.argv[1]
    car_dict = load_json(filename)
    board_game = Board()
    for key in car_dict:
        if len(car_dict[key]) != 3:
            continue
        length = car_dict[key][0]
        location = car_dict[key][1]
        orientation = car_dict[key][2]
        if key not in VALID_CAR_NAME:
            continue
        if type(length) != int:
            continue
        if len(location) != 2 or type(location) != list:
            continue
        if length < MIN_LENGTH or length > MAX_LENGTH:
            continue
        if not (orientation in VALID_ORIENTATION):
            continue
        if location == [3, 6] and orientation == 1:
            continue
        location = tuple(location)
        key = Car(key, length, location, orientation)
        board_game.add_car(key)
    game = Game(board_game)
    game.play()

