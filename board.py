
class Board:
    """
    the class board is a class that represent an (m*n) board size,
    it contains a list of the objects on the board. and by methods can ask
    from the objects to act
    """

    EMPTY_CELL = ' _ '
    BOARD_HEIGHT = 7
    BOARD_WIDTH = 7
    TARGET_CELL = (3, 7)

    def __init__(self):
        """constructor of the class"""
        self.__height = Board.BOARD_HEIGHT
        self.__width = Board.BOARD_WIDTH
        self.__cars = []
        self.__targetcell = Board.TARGET_CELL


    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """

        str_board = '\n'
        count = 0
        for cell in self.cell_list():
            if cell == self.__targetcell:
                continue
            if self.cell_content(cell) is None:
                str_board += Board.EMPTY_CELL
            else:
                str_board += (' ' + self.cell_content(cell) + ' ')
            count += 1
            if count % self.__width == 0:
                str_board += '\n'

        return str_board

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """

        cell_lst = []
        for n in range(self.__height):
            for i in range(self.__width):
                coordinate = (n, i)
                cell_lst.append(coordinate)
        cell_lst.append(self.__targetcell)
        return cell_lst

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """

        possible_move_lst = []
        for car in self.__cars:
            move_dict = car.possible_moves()
            for key in move_dict:
                cell = car.movement_requirements(key)[0]
                if self.check_validation_cell(cell):
                    temp_tuple = (car.get_name(), key, move_dict[key])
                    possible_move_lst.append(temp_tuple)
        return possible_move_lst

    def target_location(self):
        """
        This function returns the coordinates of the location which is to
        be filled for victory.
        :return: (row,col) of goal location
        """

        return self.__targetcell

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """

        for car in self.__cars:
            for coord in car.car_coordinates():
                if coordinate == coord:
                    return car.get_name()
        return

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        for cars in self.__cars:
            if cars.get_name() == car.get_name():
                return False
        for coord in car.car_coordinates():
            if not self.check_validation_cell(coord):
                return False
        self.__cars.append(car)
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """

        car = self.name_to_object(name)
        if car is False:
            return False
        else:
            for tup in self.possible_moves():
                first, second, third = tup
                if (name, movekey) == (first, second):
                    car.move(movekey)
                    return True
        return False

    def occupied_list(self):
        """

        :return return a list that contains all the coordinate that the
        objects on
        """
        cell_list = []
        for car in self.__cars:
            for coordinate in car.car_coordinates():
                cell_list.append(coordinate)
        return cell_list

    def check_validation_cell(self, coord):
        """

        :param coord:
        check if the cell is occupied or it not on the board
        :return: true for empty and false for occupied or not on the board
        """
        if coord in self.occupied_list() or coord not in self.cell_list():
            return False
        return True

    def name_to_object(self, name):
        """

        :param name:
        :return: the object with the name
        """
        for car in self.__cars:
            if name == car.get_name():
                return car
        return False
