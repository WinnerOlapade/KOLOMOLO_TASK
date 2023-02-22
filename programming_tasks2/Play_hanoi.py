# def game_state():
#     start_game = input("Would you like to play Hanoi's Tower? Enter 'Yes' to begin game: ")
#     print()

#     # Prompt user to play game
#     while start_game.lower() not in ["yes", "no"]:
#         print("Wrong input! (º_º). Please enter 'yes' or 'no'. ")
#         print()
#         start_game = input("Would you like to play Hanoi's Tower? Enter 'Yes' to begin game: ")

#     if start_game.lower() == "yes":
#         while True:
#             try:
#                 print()
#                 disc = int(input("Enter the number of DISCS from [2 to 7]: "))
#                 if 2 <= disc <= 7:
#                     break
#                 else:
#                     print("Invalid input, please enter a number between 2 and 7. ")
#             except ValueError:
#                 print("Invalid input, please enter an integer. ")

#         while True:
#             try:
#                 stack = int(input("Enter the number of STACKS from [3 to 4]: "))
#                 if 3 <= stack <= 4:
#                     break
#                 else:
#                     print("Invalid input, please enter a number between 3 and 4. ")
#             except ValueError:
#                 print("Invalid input, please enter an integer. ")         
                

#     elif start_game.lower() == "no":
#         print("Okay, maybe next time! (^_^) ")
#         return
        
#     # initialize tower before game begins 
#     tower = [[] for _ in range(stack)]
    
#     # add the disks to the first rod
#     for disk in range(disc, 0, -1):
#         tower[0].append(disk)
#     print(f"Starting game state: {tower}")

#     # request moves
#     start_tower = int(input("Enter tower to Move From: "))
#     end_tower = int(input("Enter tower to Move To: "))
#     game_moves = [start_tower, end_tower]

#     for begin, end in game_moves:
#         moving_disk = tower[begin-1].pop()
#         print(f"Moving disk of size {moving_disk} from tower {begin} to tower {end}")
#         tower[end-1].append(moving_disk)

#         if not tower[end-1] == sorted(tower[end-1], reverse=True):
#             print("Illegal move, Game over!!!")
#             return
#     else:
#         print("Winner Winner, chicken dinner")

# game_state()