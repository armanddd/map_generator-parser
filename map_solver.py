class SolveMap:

    def __init__(self, my_map):
        self._final_output = ""
        self._map_content = my_map.get_file_content()
        self._map_width = my_map.get_width()
        self._map_height = my_map.get_height()
        self._path_character = my_map.get_path_character()
        self._goal_character = my_map.get_goal_character()
        self._obstacle_character = my_map.get_obstacle_character()
        self._actual_position_x = my_map.get_starting_position_x()
        self._actual_position_y = my_map.get_starting_position_y()
        self._goal_position_x = my_map.get_goal_position_x()
        self._goal_position_y = my_map.get_goal_position_y()
        self._line_left_counter = 0
        self._line_right_counter = 0
        self._only_one_way = True

    def solve_map(self):
        print(self._map_content)
        print("\nactual position x:", self._actual_position_x, "\nactual positon y :", self._actual_position_y,
              "\ngoal position x:", self._goal_position_x, "\ngoal position y:", self._goal_position_y)
        map_tab = self._map_content.splitlines()

        # solving loop
        while True:

            # case where it ends
            if (self._actual_position_x == self._goal_position_x) and (self._actual_position_y == self._goal_position_y):
                print("we are at the goal position !! ", self._final_output)
                break

            # case 1 if char from bottom is path character
            if map_tab[self._actual_position_y + 1][self._actual_position_x] == self._path_character or map_tab[self._actual_position_y + 1][self._actual_position_x] == self._goal_character:
                self._actual_position_y += 1
                self._final_output += "B"
                print("actual y pos : ", self._actual_position_y, "actual x pos : ", self._actual_position_x)
                print("going down")
                continue

            # case 2 where bottom is obstacle character and have to check left/right for better option
            if map_tab[self._actual_position_y + 1][self._actual_position_x] == self._obstacle_character and self._actual_position_y != self._map_height - 2:

                # last constant(2) is the index shift plus the last obstacle
                right_iterations_max = self._map_width - self._actual_position_x - 2
                right_iterations = 0
                # last constant(3) is the index shift, the first obstacle and my own character
                left_iterations_max = self._map_width - right_iterations_max - 3
                left_iterations = 0

                print("right iterations max : ", right_iterations_max, "|| left iterations max : ", left_iterations_max)

                while right_iterations <= right_iterations_max and right_iterations_max > 0:
                    if map_tab[self._actual_position_y][self._actual_position_x + right_iterations] == self._path_character \
                            and map_tab[self._actual_position_y + 1][self._actual_position_x + right_iterations] == self._path_character:
                        break
                    right_iterations += 1

                while left_iterations <= left_iterations_max and left_iterations_max > 0:
                    if map_tab[self._actual_position_y][self._actual_position_x - left_iterations] == self._path_character \
                            and map_tab[self._actual_position_y + 1][self._actual_position_x - left_iterations] == self._path_character:
                        break
                    left_iterations += 1
                print("at the end, my right iterator is : ", right_iterations, " and my left iterator is : ", left_iterations)

                if right_iterations < left_iterations and right_iterations != 0:
                    # here we go right (shorter path)
                    self._actual_position_x = self._actual_position_x + right_iterations
                    self._final_output = self._final_output + ("R" * right_iterations)
                    print("going right is better, cause right iterations: ", right_iterations, "and left iterations: ", left_iterations)
                    left_iterations = 0
                    right_iterations = 0

                elif right_iterations > left_iterations and left_iterations != 0:
                    # here we go left (shorter path)
                    self._actual_position_x = self._actual_position_x - left_iterations
                    self._final_output = self._final_output + ("L" * left_iterations)
                    print("going left is better, cause right iterations: ", right_iterations, "and left iterations: ", left_iterations)
                    left_iterations = 0
                    right_iterations = 0

                elif right_iterations > left_iterations:
                    # here we go right (shorter path)(case where starting position is near wall)
                    self._actual_position_x = self._actual_position_x + right_iterations
                    self._final_output = self._final_output + ("R" * right_iterations)
                    print("going right2 is better, cause right iterations: ", right_iterations, "and left iterations: ", left_iterations)
                    left_iterations = 0
                    right_iterations = 0

                elif right_iterations < left_iterations:
                    # here we go left (shorter path)(case where starting position is near wall)
                    self._actual_position_x = self._actual_position_x - left_iterations
                    self._final_output = self._final_output + ("L" * left_iterations)
                    print("going left2 is better, cause right iterations: ", right_iterations, "and left iterations: ", left_iterations)
                    left_iterations = 0
                    right_iterations = 0

                elif right_iterations == left_iterations and left_iterations > 0:
                    # here we go right or left (depending on w.e will get me closer to the goal position)
                    if (self._actual_position_x > self._goal_position_x):
                        self._actual_position_x = self._actual_position_x - right_iterations
                        self._final_output = self._final_output + ("L" * right_iterations)
                        print("going right and left is same(here i choose left), cause right iterations: ", right_iterations, "and left iterations: ", left_iterations)
                    else:
                        self._actual_position_x = self._actual_position_x + right_iterations
                        self._final_output = self._final_output + ("R" * right_iterations)
                        print("going right and left is same(here i choose right), cause right iterations: ", right_iterations, "and left iterations: ", left_iterations)
                    left_iterations = 0
                    right_iterations = 0

            # case 3 where both actual position and goal position are on same height(line), but not same width
            if self._actual_position_y == self._goal_position_y and self._actual_position_x > self._goal_position_x:
                print("ben la jrenntr dans le premier if")
                while self._actual_position_x > self._goal_position_x:
                    self._actual_position_x -= 1
                    self._final_output += "L"
                print(self._final_output)
                break
            if self._actual_position_y == self._goal_position_y and self._actual_position_x < self._goal_position_x:
                print("ben la jrentr dans le deuxieme if")
                while self._actual_position_x < self._goal_position_x:
                    self._actual_position_x += 1
                    self._final_output += "R"
                print(self._final_output)
                break



        # print(map_tab[self._actual_position_y][self._actual_position_x], "***")
        '''
        for line in map_tab:
            for char in line:
                print(char, "||")
        '''
        # print(map_tab)
        # print(map_tab.__class__)

