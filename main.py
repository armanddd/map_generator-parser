from map_generator import GenerateMap
from map_solver import SolveMap
import map_drawer as draw

if __name__ == "__main__":
    choice = None

    while choice is not '1' and choice is not '2':
        choice = input("Please make a choice(1 for creating map, 2 for importing map) : ")
        if choice == '1':
            map_file_name = input("Please type the name of the file for your map : ")
            map_max_width = int(input("Please input the maximum width of the map : "))
            map_max_height = int(input("Please input the maximum height of the map : "))
            map_player_character = input("Please input the player character : ")
            map_goal_character = input("Please input the goal character : ")
            map_obstacle_character = input("Please input the obstacle character : ")
            map_path_character = input("Please input the path character : ")

            my_map = GenerateMap(map_file_name, map_max_width, map_max_height, map_player_character, map_goal_character, map_obstacle_character, map_path_character)
            my_solved_map = SolveMap(my_map).solve_map()
            draw.draw_map(my_solved_map.get_original_map(), my_solved_map.get_map_width(), my_solved_map.get_map_height(), my_solved_map.get_obstacle_character(),
                          my_solved_map.get_final_output(), my_solved_map.get_starting_position_x(), my_solved_map.get_starting_position_y())
        elif choice == '2':
            map_path = input("Please enter the name of the map : ")
            my_solved_map = SolveMap(map_path)
            my_solved_map.solve_map()
            draw.draw_map(my_solved_map.get_original_map(), my_solved_map.get_map_width(), my_solved_map.get_map_height(), my_solved_map.get_obstacle_character(),
                          my_solved_map.get_final_output(), my_solved_map.get_starting_position_x(), my_solved_map.get_starting_position_y())
