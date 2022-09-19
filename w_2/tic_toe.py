from termcolor import colored

def main():
    # Author: Josué B. Centurión  

    my_list = ["1","2","3",
    "4","5","6",
    "7","8","9"]

    winner = ""
    current_player = "x"
    while winner == "": 

        if (my_list[0] == my_list[1] and my_list[1] == my_list[2]) or (my_list[2] == my_list[5] and my_list[5] == my_list[8]) or (my_list[0] == my_list[3] and my_list[3] == my_list[6]) or (my_list[6] == my_list[7] and my_list[7] == my_list[8]) or (my_list[0] == my_list[4] and my_list[4] == my_list[8]) or (my_list[2] == my_list[4] and my_list[4] == my_list[6]) or (my_list[3] == my_list[4] and my_list[4] == my_list[5]) :
            if current_player == "o":
                winner = "X"
            else:
                winner = "O"

        else: 
            print_tic_toe(my_list)

            user_input = input(f"\n{current_player}'s turn to choose a square (1-9):")
            for i , v in enumerate(my_list):
                if v == user_input : 
                    my_list[i] = current_player
                    if current_player == "x":
                        current_player = "o"
                    else:
                        current_player = "x"

        
    print_tic_toe(my_list)
    print()
    print()
    print(colored(f"The winner is {winner} $☻♥ ","blue","on_white"))
    print()


def print_tic_toe(my_list): 
    for i , v in enumerate(my_list):
        i += 1
        if i % 3 == 0:
            if v == "x":
                print(colored(f"{v}","blue"), end='')
            elif v == "o":
                print(colored(f"{v}","red"), end='')
            else: 
                print(f"{v}", end='')
                
            if i == 3 or i == 6 :
                print("\n-+-+-")
        else:
            if v == "x":
                print(colored(f"{v}|","blue"), end='')
            elif v == "o":
                print(colored(f"{v}|","red"), end='')
            else:
                print(f"{v}|", end='')

main()

""" Steps: 
1) 9 elem my_list 
2) how to print 
3) select specific number & make x or o
4) make first choose x than o  
5) Display in the console

while loop (i: finish the game )  
 """



