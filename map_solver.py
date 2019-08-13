class SolveMap:

    def __init__(self, my_map):

        if isinstance(my_map, str):
            try:
                self._map_content = open(my_map, "r").read()
                self._immutable_map_content = self._map_content
            except IOError as e:
                print(e)
            self._final_output = ""
            self._map_width = SolveMap.__find_map_width(self)
            self._map_height = SolveMap.__find_map_height(self)
            self._path_character, self._obstacle_character = SolveMap.__find_path_obstacle_character(self)
            self._player_character, self._goal_character = SolveMap.__find_goal_player_character(self)
            self._starting_position_x, self._starting_position_y = SolveMap.__find_actual_position_xy(self)
            self._actual_position_x, self._actual_position_y = SolveMap.__find_actual_position_xy(self)
            self._goal_position_x, self._goal_position_y = SolveMap.__find_goal_position_xy(self)
            self._line_left_counter = 0
            self._line_right_counter = 0
            self._only_one_way = True
            # here we have a tuple where we keep all the location where we changed the path to obstacle
            self._obstacle_to_path_changes = ()
        else:
            try:
                self._map_content = my_map.get_file_content()
                self._immutable_map_content = self._map_content
            except Exception as e:
                print(e)
            self._final_output = ""
            self._map_width = my_map.get_width()
            self._map_height = my_map.get_height()
            self._path_character = my_map.get_path_character()
            self._goal_character = my_map.get_goal_character()
            self._obstacle_character = my_map.get_obstacle_character()
            self._starting_position_x, self._starting_position_y = my_map.get_starting_position_x(), my_map.get_starting_position_y()
            self._actual_position_x = my_map.get_starting_position_x()
            self._actual_position_y = my_map.get_starting_position_y()
            self._goal_position_x = my_map.get_goal_position_x()
            self._goal_position_y = my_map.get_goal_position_y()
            self._line_left_counter = 0
            self._line_right_counter = 0
            self._only_one_way = True
            # here we have a tuple where we keep all the location where we changed the path to obstacle
            self._obstacle_to_path_changes = ()

    def solve_map(self):
        print(self._map_content)
        # print("\nactual position x:", self._actual_position_x, "\nactual positon y :", self._actual_position_y,
        #      "\ngoal position x:", self._goal_position_x, "\ngoal position y:", self._goal_position_y)
        map_tab = self._map_content.splitlines()

        # solving loop
        while True:

            # case where it ends(and directly falls onto the good column from upper)
            if (self._actual_position_x == self._goal_position_x) and (self._actual_position_y == self._goal_position_y):
                print("we are at the goal position !! ", self._final_output)
                break

            # case 1 if char from bottom is path character
            if map_tab[self._actual_position_y + 1][self._actual_position_x] == self._path_character or map_tab[self._actual_position_y + 1][self._actual_position_x] == self._goal_character:
                self._actual_position_y += 1
                self._final_output += "B"
                # print("actual y pos : ", self._actual_position_y, "actual x pos : ", self._actual_position_x)
                # print("going down")
                continue

            # case 2 where bottom is obstacle character and have to check left/right for better option
            if (map_tab[self._actual_position_y + 1][self._actual_position_x] == self._obstacle_character and self._actual_position_y != self._map_height - 2) or 1 == 2:

                # last constant(2) is the index shift plus the last obstacle
                right_iterations_max = self._map_width - self._actual_position_x - 2
                right_iterations = 0
                # last constant(3) is the index shift, the first obstacle and my own character
                left_iterations_max = self._map_width - right_iterations_max - 3
                left_iterations = 0

                # print("right iterations max : ", right_iterations_max, "|| left iterations max : ", left_iterations_max)

                while right_iterations <= right_iterations_max and right_iterations_max > 0:
                    if map_tab[self._actual_position_y][self._actual_position_x + right_iterations] == self._path_character \
                            and map_tab[self._actual_position_y + 1][self._actual_position_x + right_iterations] == self._path_character:
                        break
                    elif map_tab[self._actual_position_y][self._actual_position_x + right_iterations] == self._obstacle_character:
                        right_iterations = 0
                        break
                    right_iterations += 1

                while left_iterations <= left_iterations_max and left_iterations_max > 0:
                    if map_tab[self._actual_position_y][self._actual_position_x - left_iterations] == self._path_character \
                            and map_tab[self._actual_position_y + 1][self._actual_position_x - left_iterations] == self._path_character:
                        break
                    elif map_tab[self._actual_position_y][self._actual_position_x - left_iterations] == self._obstacle_character:
                        left_iterations = 0
                        break
                    left_iterations += 1
                # print("at the end, my right iterator is : ", right_iterations, " and my left iterator is : ", left_iterations)

                # case where it's a full obstacle row
                if right_iterations == 0 and left_iterations == 0:
                    self._obstacle_to_path_changes = (self._actual_position_x, self._actual_position_y)
                    # print("jprint map tab ici:", map_tab.__class__, "  ", map_tab)
                    # print("jprint map tab ici:", map_tab[self._actual_position_y].__class__, "  ", map_tab[1])
                    new_str = map_tab[self._actual_position_y][:self._actual_position_x] + self._obstacle_character + map_tab[self._actual_position_y][self._actual_position_x + 1:]
                    map_tab[self._actual_position_y] = new_str
                    self._final_output = self._final_output[:-1]
                    # print("jprint newstr ici:", new_str.__class__, "  ", new_str)
                    self._actual_position_y -= 1
                    # print(self._obstacle_to_path_changes)
                    continue
                # case where it's a full obstacle row

                if right_iterations < left_iterations and right_iterations != 0:
                    # here we go right (shorter path)
                    self._actual_position_x = self._actual_position_x + right_iterations
                    self._final_output = self._final_output + ("R" * right_iterations)
                    # print("going right is better, cause right iterations: ", right_iterations, "and left iterations: ", left_iterations)
                    left_iterations = 0
                    right_iterations = 0

                elif right_iterations > left_iterations and left_iterations != 0:
                    # here we go left (shorter path)
                    self._actual_position_x = self._actual_position_x - left_iterations
                    self._final_output = self._final_output + ("L" * left_iterations)
                    # print("going left is better, cause right iterations: ", right_iterations, "and left iterations: ", left_iterations)
                    left_iterations = 0
                    right_iterations = 0

                elif right_iterations > left_iterations:
                    # here we go right (shorter path)(case where starting position is near wall)
                    self._actual_position_x = self._actual_position_x + right_iterations
                    self._final_output = self._final_output + ("R" * right_iterations)
                    # print("going right2 is better, cause right iterations: ", right_iterations, "and left iterations: ", left_iterations)
                    left_iterations = 0
                    right_iterations = 0

                elif right_iterations < left_iterations:
                    # here we go left (shorter path)(case where starting position is near wall)
                    self._actual_position_x = self._actual_position_x - left_iterations
                    self._final_output = self._final_output + ("L" * left_iterations)
                    # print("going left2 is better, cause right iterations: ", right_iterations, "and left iterations: ", left_iterations)
                    left_iterations = 0
                    right_iterations = 0

                elif right_iterations == left_iterations and left_iterations > 0:
                    # here we go right or left (depending on w.e will get me closer to the goal position)
                    if self._actual_position_x > self._goal_position_x:
                        self._actual_position_x = self._actual_position_x - right_iterations
                        self._final_output = self._final_output + ("L" * right_iterations)
                        # print("going right and left is same(here i choose left), cause right iterations: ", right_iterations, "and left iterations: ", left_iterations)
                    else:
                        self._actual_position_x = self._actual_position_x + right_iterations
                        self._final_output = self._final_output + ("R" * right_iterations)
                        # print("going right and left is same(here i choose right), cause right iterations: ", right_iterations, "and left iterations: ", left_iterations)
                    left_iterations = 0
                    right_iterations = 0

            # case 3 where both actual position and goal position are on same height(line), but not same width
            if self._actual_position_y == self._goal_position_y and self._actual_position_x > self._goal_position_x:
                # print("ben la jrenntr dans le premier if")
                while self._actual_position_x > self._goal_position_x:
                    self._actual_position_x -= 1
                    self._final_output += "L"
                print(self._final_output)
                break
            if self._actual_position_y == self._goal_position_y and self._actual_position_x < self._goal_position_x:
                # print("ben la jrentr dans le deuxieme if")
                while self._actual_position_x < self._goal_position_x:
                    self._actual_position_x += 1
                    self._final_output += "R"
                print(self._final_output)
                break

    def __find_map_width(self):
        counter = 0
        while self._map_content[counter] != '\n':
            counter += 1
        return counter

    def __find_map_height(self):
        counter = 0
        for char in self._map_content:
            if char == '\n':
                counter += 1
        return counter

    def __find_path_obstacle_character(self):
        map_tab = self._map_content.splitlines()
        obstacle_character = map_tab[0][0]
        if map_tab[1][1] == map_tab[1][self._map_width - 1]:
            path_character = map_tab[1][1]
        else:
            path_character = map_tab[1][self._map_width - 2]
        return path_character, obstacle_character

    def __find_goal_player_character(self):
        map_tab = self._map_content.splitlines()

        player_counter = 1
        while map_tab[1][player_counter] == self._path_character:
            player_counter += 1
        player_character = map_tab[1][player_counter]

        goal_counter = 1
        while map_tab[self._map_height - 2][goal_counter] == self._path_character:
            goal_counter += 1
        goal_character = map_tab[self._map_height - 2][goal_counter]

        return player_character, goal_character

    def __find_actual_position_xy(self):
        map_tab = self._map_content.splitlines()
        counter = 1
        while map_tab[1][counter] != self._player_character:
            counter += 1
        return counter, 1

    def __find_goal_position_xy(self):
        map_tab = self._map_content.splitlines()
        counter = 1
        while map_tab[self._map_height - 2][counter] != self._goal_character:
            counter += 1
        return counter, self._map_height - 2

    def get_original_map(self):
        return self._immutable_map_content

    def get_map_width(self):
        return self._map_width

    def get_map_height(self):
        return self._map_height

    def get_obstacle_character(self):
        return self._obstacle_character

    def get_starting_position_x(self):
        return self._starting_position_x

    def get_starting_position_y(self):
        return self._starting_position_y

    def get_final_output(self):
        return self._final_output

        # print(map_tab[self._actual_position_y][self._actual_position_x], "***")
        # print(map_tab)
        # print(map_tab.__class__)
