import random


class GenerateMap:
    def __init__(self, file_path, width, height, player_character, goal_character, obstacle_character, path_character):
        self._file = open(file_path, "w")
        self._file_content = ""
        self._width = width
        self._height = height
        self._player_character = player_character
        self._goal_character = goal_character
        self._obstacle_character = obstacle_character
        self._path_character = path_character
        self._onlyOnePlayerCheck = True
        self._onlyOneGoalCheck = True
        self._starting_position_x = 0
        self._starting_position_y = 1
        self._goal_position_x = 0
        self._goal_position_y = self._height - 2

        # done for stability
        self._randomVariable = random.randint(1, self._width - 2)

        for height in range(self._height):
            for width in range(self._width):
                if height == 0 or height == self._height - 1:
                    self._file_content += obstacle_character
                    if width == self._width - 1:
                        self._file_content += "\n"
                    continue
                if width == 0 or width == self._width - 1:
                    self._file_content += obstacle_character
                    if width == self._width - 1:
                        self._file_content += "\n"
                else:
                    if height == 1 and width == self._randomVariable and self._onlyOnePlayerCheck is True:
                        self._file_content += player_character
                        self._starting_position_x = self._randomVariable
                        self._randomVariable = random.randint(1, self._width - 2)
                        self._onlyOnePlayerCheck = False
                        continue
                    if height == self._height - 2 and width == self._randomVariable and self._onlyOneGoalCheck is True:
                        self._file_content += goal_character
                        self._goal_position_x = self._randomVariable
                        self._onlyOneGoalCheck = False
                        continue
                    if random.choice([random.randint(0, 4)] * 3) == 2 and height != 1 and height != self._height - 2:
                        self._file_content += obstacle_character
                    else:
                        self._file_content += path_character
        self._file.write(self._file_content)
        self._file.close()

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_starting_position_x(self):
        return self._starting_position_x

    def get_starting_position_y(self):
        return self._starting_position_y

    def get_goal_position_x(self):
        return self._goal_position_x

    def get_goal_position_y(self):
        return self._goal_position_y

    def get_player_character(self):
        return self._player_character

    def get_goal_character(self):
        return self._goal_character

    def get_obstacle_character(self):
        return self._obstacle_character

    def get_path_character(self):
        return self._path_character

    def get_file_content(self):
        return self._file_content

    def __repr__(self):
        return f'Object:GenerateMap->{{\n\tself_width:{self._width},\n\tself_height:{self._height},\n\tself_starting_position_x,y:[{self._starting_position_x},' \
            f'{self._starting_position_y}],\n\tself_goal_position_x,y:[{self._goal_position_x},{self._goal_position_y}],\n' \
            f'\tself_player_character:\'{self._player_character}\',\n\tself_goal_character:\'{self._goal_character}\', \n\tself_obstacle_character:\'{self._obstacle_character}\',' \
            f' \n\tself_path_character:\'{self._path_character}\'\n}}'

    @classmethod
    def generate_standard_map(cls):
        return cls("map.txt", 10, 10, "x", "o", "#", ".")

