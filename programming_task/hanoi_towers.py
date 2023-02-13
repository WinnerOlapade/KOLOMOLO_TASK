"""
hanoi_tower() = takes in 6 parameters : num_discs, source, auxiliary1, auxiliary2, destination, stacks
num_discs = number of discs to be moved
source = starting stack with all num_discs
auxiliary1 = first temporary stack
auxiliary2 = second temporary stack
destination = final stack where gameis solved
stacks = a dictionary containing the num_stacks (with keys representing the names and values being lists representing the discs on each stack).
"""


def hanoi_tower(num_discs, source, auxiliary1, auxiliary2, destination, stacks):

    if num_discs == 1:
        if len(stacks[destination - 1]) > 0 and stacks[source - 1][-1] > stacks[destination - 1][-1]:
            print(f"Player Moved from Tower {disc} to Tower  {tower},")
            print(f"Illegal: cannot move from {disc} onto smaller disc {tower} at step {move} stacks: {stacks}.")
            print("Failed! Not all discs were moved to the destination !!!")
            exit()
        stacks[destination - 1].append(stacks[source - 1].pop())
        return

    hanoi_tower(num_discs-2, source, auxiliary2, destination, auxiliary1, stacks)

    if len(stacks[auxiliary2 - 1]) > 0 and stacks[source - 1][-1] > stacks[auxiliary2 - 1][-1]:
        print(f"Player Moved from Tower {disc} to Tower  {tower},")
        print(f"Illegal: cannot move from {disc} onto smaller disc {tower} at step {move} stacks: {stacks}.")
        print("Failed! Not all discs were moved to the destination !!!")
        exit()
    stacks[auxiliary2 - 1].append(stacks[source - 1].pop())

    if len(stacks[destination - 1]) > 0 and stacks[source - 1][-1] > stacks[destination - 1][-1]:
        print(f"Player Moved from Tower {disc} to Tower  {tower},")
        print(f"Illegal: cannot move from {disc} onto smaller disc {tower} at step {move} stacks: {stacks}.")
        print("Failed! Not all discs were moved to the destination !!!")
        exit()
    stacks[destination - 1].append(stacks[source - 1].pop())

    if len(stacks[destination - 1]) > 0 and stacks[auxiliary2 - 1][-1] > stacks[destination - 1][-1]:
        print(f"Player Moved from Tower {disc} to Tower  {tower},")
        print(f"Illegal: cannot move from {disc} onto smaller disc {tower} at step {move} stacks: {stacks}.")
        print("Failed! Not all discs were moved to the destination !!!")
        exit()
    stacks[destination - 1].append(stacks[auxiliary2 - 1].pop())

    hanoi_tower(num_discs-2, auxiliary1, source, auxiliary2, destination, stacks)


print("Welcome to Hanoi Towers !!!")
print()
with open(input("Enter input file name: "), 'r') as file:
    
    num_discs, num_stacks = map(int, file.readline().split())

    stacks = [[] for _ in range(num_stacks)]
    for i in range(num_discs, 0, -1):
        stacks[0].append(i)
    print(f"Starting Stack: {stacks}")

    for move, line in enumerate(file, start=2):
        disc, tower = map(int, line.split())
        hanoi_tower(1, disc, 6-disc-tower, tower, tower, stacks)
        print(disc, tower)
        
        print(f"Player Moved from Tower {disc} to Tower  {tower},")
        print(f" New Stack: {stacks}")
        
    if len(stacks[-1]) == num_discs:
        print("Congratulations! You have solved the puzzle !!! :)")
    else:
        print("Failed! Not all discs were moved to the destination !!!")

