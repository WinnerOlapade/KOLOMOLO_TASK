def read_input_file(input_file):
    with open(input_file, 'r') as file:
       game_data = file.read()
    return game_data
    

def game_state():
    file_name = input("Please enter the name of the file you wish to read: ")
    game_data_raw = read_input_file(file_name)
    game_data = [[int(x) for x in y.split(" ")] for y in game_data_raw.split("\n")]

    # remove the init line
    number_disk, number_stack = game_data.pop(0)
    
    # initialize rods before game begins 
    rods = [[] for _ in range(number_stack)]
    
    # add the disks to the first rod
    for disk in range(number_disk, 0, -1):
        rods[0].append(disk)

    for begin, end in game_data:
        moving_disk = rods[begin-1].pop()
        print(f"Moving disk of size {moving_disk} from tower {begin} to tower {end}")
        rods[end-1].append(moving_disk)

        if not rods[end-1] == sorted(rods[end-1], reverse=True):
            print("Illegal move, Game over!!!")
            return
    else:
        print("Winner Winner, chicken dinner")

game_state()