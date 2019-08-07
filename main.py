from map_generator import GenerateMap
from map_solver import SolveMap


'''
for i in file_content:
    for x in i:
        print(x)
    #print(i)
'''


#print(starting_position_x, starting_position_y)
#print(ending_position_x, ending_position_y)

if __name__ == "__main__":
    map_file_name = input("Please type the name of the file for your map : ")
    map_max_width = int(input("Please input the maximum width of the map : "))
    map_max_height = int(input("Please input the maximum height of the map : "))
    map_player_character = input("Please input the player character : ")
    map_goal_character = input("Please input the goal character : ")
    map_obstacle_character = input("Please input the obstacle character : ")
    map_path_character = input("Please input the path character : ")

    my_map = GenerateMap(map_file_name, map_max_width, map_max_height, map_player_character, map_goal_character, map_obstacle_character, map_path_character)

    my_solved_map = SolveMap(my_map).solve_map()

'''
    starting_position_x, starting_position_y = GetStartingPos.get_starting_position(my_map)
    ending_position_x, ending_position_y = GetStartingPos.get_ending_position(my_map)


    moving_position_x = starting_position_x
    moving_position_y = starting_position_y

    triesCounter = 1
    tries = {'Try_0': Try()}

    while tries["Try_" + str(triesCounter)].movingNodes > 1:
        tries["Try_" + str(triesCounter)] = Try()
        triesCounter += 1
        tries['Try_0'].movingNodes -= 1
'''

'''
all_options = {}
all_options[repr([moving_position_x, moving_position_y])] = moving_option

print(all_options)
'''

