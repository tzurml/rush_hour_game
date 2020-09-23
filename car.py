class Car:
    """
    class is car. its defines a car with by: name, length, location
     ,orientation. and methods that or return data on the car or change the
     car location
    """
    # valid moves
    UP = 'u'
    DOWN = 'd'
    RIGHT = 'r'
    LEFT = 'l'

    # valid orientation
    HORIZONTAL = 1
    VERTICAL = 0

    # key = move, value = description
    DICT_POSSIBLE_MOVE = {DOWN: "the car can move down",
                          UP: "the car can move up",
                          RIGHT: "the car can move to the right",
                          LEFT: "the car can move to the left"}

    # key = orientation. value = [possible moves]
    DICT_ORIENTATION_MOVE = {0: [DOWN, UP],
                             1: [RIGHT, LEFT]}

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """

        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """

        row, column = self.__location
        if self.__orientation == Car.VERTICAL:
            return [(i, column) for i in range(row, row + self.__length)]
        if self.__orientation == Car.HORIZONTAL:
            return [(row, i) for i in range(column, column + self.__length)]

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """

        possible_dict = dict()
        for move in Car.DICT_ORIENTATION_MOVE[self.__orientation]:
            possible_dict[move] = Car.DICT_POSSIBLE_MOVE[move]
        return possible_dict

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for
        this move to be legal.
        """

        movement_requirements_lst = []
        lst_locations = self.car_coordinates()
        start_row, start_column = self.__location
        end_row, end_column = lst_locations[-1]
        down = (end_row+1, end_column)
        up = (start_row-1, start_column)
        right = (end_row, end_column+1)
        left = (start_row, start_column-1)
        if movekey == Car.UP:
            movement_requirements_lst.append(up)
        if movekey == Car.DOWN:
            movement_requirements_lst.append(down)
        if movekey == Car.LEFT:
            movement_requirements_lst.append(left)
        if movekey == Car.RIGHT:
            movement_requirements_lst.append(right)
        return movement_requirements_lst

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        change the car location
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        row, column = self.__location
        if movekey in self.possible_moves():
            if self.__orientation == Car.VERTICAL:
                if movekey == Car.DOWN:
                    self.__location = (row + 1, column)
                elif movekey == Car.UP:
                    self.__location = (row - 1, column)
            if self.__orientation == Car.HORIZONTAL:
                if movekey == Car.RIGHT:
                    self.__location = (row, column + 1)
                elif movekey == Car.LEFT:
                    self.__location = (row, column - 1)
            return True

        return False

    def get_name(self):
        """
        :return: The name of this car.
        """

        return self.__name
