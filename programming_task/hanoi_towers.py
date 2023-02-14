def validate_move(start_tower, end_tower, moves, stacks):
    """Validate the move of the disc to the tower."""
    if len(stacks[end_tower-1]) > 0 and stacks[start_tower-1][-1] > stacks[end_tower-1][-1]: #this comapres size of disk in starting 
        print(f"Player moved from Tower {start_tower} to Tower {end_tower},")
        print(f"Illegal: cannot move from {start_tower} onto  {end_tower}  stacks: {stacks}.")
        print("Failed! Not all discs were moved to the destination!!!")
        exit()
    stacks[end_tower-1].append(stacks[start_tower-1].pop())

def hanoi_tower(given_disc, source, auxiliary1, auxiliary2, destination, stacks):
    """Move the discs in the game of Hanoi Tower."""
    if given_disc == 1:
        validate_move(source, destination, 1, stacks)
        return

    hanoi_tower(given_disc-2, source, auxiliary2, destination, auxiliary1, stacks)

    validate_move(source, auxiliary2, given_disc, stacks)
    validate_move(source, destination, given_disc, stacks)
    validate_move(auxiliary2, destination, given_disc, stacks)

    hanoi_tower(given_disc-2, auxiliary1, source, auxiliary2, destination, stacks)

def read_input_file(input_file):
    with open(input_file, 'r') as file:
        given_disc, given_stacks = map(int, file.readline().split())

        moves = []
        for line in file:
            start_tower, end_tower = map(int, line.split())
            moves.append((start_tower, end_tower))
    return given_disc, given_stacks, moves

def play_hanoi_tower():
    """Play the Hanoi Tower game with the input file."""
    input_file = input("Enter filename: ")
    given_disc, given_stacks, moves = read_input_file(input_file)

    stacks = [[] for _ in range(given_stacks)]
    for i in range(given_disc, 0, -1):
        stacks[0].append(i)
    print(f"Starting Stack: {stacks}")

    for move, (start_tower, end_tower) in enumerate(moves, start=1):
        hanoi_tower(1, start_tower, 6-start_tower-end_tower, end_tower, end_tower, stacks)
        print(f"Player moved from Tower {start_tower} to Tower {end_tower},")
        print(f"New Stack: {stacks}")
    


    if len(stacks[-1]) == given_disc:
        print("Congratulations! You have solved the puzzle!!! :)")
    else:
        print("Failed! Not all discs were moved to the destination!!!")
play_hanoi_tower()