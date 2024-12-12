import random
import os

data_file = "game_data.txt"
hscore_file = "hscore_data.txt"
game_data = {}
hscore_data = {}
valids = "1234567890abcdefghijklmnopqrstuvwxyz"
def menu():
    print("Welcome")
    while True:
        mode = input("\nMain Menu:\n1) Start Game\n2) Resume\n3) Leaderboards\n4) Game Mechanics\n5) Quit\nEnter Selection Here: ")
        if mode == "1": 
            start_game()
        elif mode == "2":
            resume_game()
        elif mode == "3":
            show_leaderboard()
        elif mode == "4":
            mechanics()
        elif mode == "5":
            print("Goodbye!")
            return
        else:
            print("Invalid input. Please enter a number from 1 to 5.")

def mechanics():
    print("""            1.) Starting the Game:
                        Enter Username: Begin by entering your username.
                        Deposit Money: You must deposit at least 5 pesos to start playing.  
            2.) Playing the Game:
                        Cups Display: Three cups (A, B, and C) will be displayed on the screen.
                        Guess the Cup: Try to guess which cup the ball is hidden under.
                        Correct Guess: If you guess correctly, you win 5 pesos, and your score increases by 5 points.
                        Incorrect Guess: If you guess incorrectly, you lose 5 pesos.
                        Game Balance: Your current earnings and wallet balance will be shown after each guess.
            3.) Pausing the Game:
                        If you need to take a break, you can pause the game by selecting the pause option (D).
                        Your game state will be saved, and you can resume later by selecting the "Re sume" option from the main menu.
            4.) Resuming the Game:
                        Resume Option: Choose the "Resume" option from the main menu and enter your username to continue a previously paused game.
                        Continue Playing: The game will resume from where you left off, with the same score and amount of money.
            5.) Winning and Losing:
                        Winning: Continue guessing correctly to increase your score and earnings.
                        Losing: If your balance falls below 5 pesos, the game will end.
            6.) Leaderboards:
                        After finishing the game, you can check the leaderboards to see the highest scores.
                        Your highest earning will be recorded if it surpasses your previous best earning.""")
    delay = input("If you Understand Press Enter to Continue: ")
    print("\n" * 100)

def start_game():
    global name, score, state, resume, money
    name = input("Please Enter your Username: ").lower()
    if name == "":
        print("\n" * 100)
        print("No Input")
        return
    for chars in name:
        if chars not in valids:
            print("\n" * 100)
            print("Warning: Invalid Username")
            return
    if os.path.exists(data_file):
        if ((f"{name}" in game_data) and (game_data[name]["state"] == "True")) == True:
            print("\n" * 100)
            print("Your Game is paused cannot start a game")
            return
    print("\n" * 100)
    score = 0
    while True:
        end = False
        money = input("Cash In: ")
        for val in money:
            if val not in "0123456789":
                end = True
                break
        if money == "":
            print("\n" * 100)
            print("No Input")
        elif end == True:
            print("\n" * 100)
            print("Invalid Input")
        elif int(money) < 5:
            print("\n" * 100)
            print("Please Put atleast 5 Pesos to play")
        else:
            break
    money = int(money)
    state = "False"
    resume = False
    game()

def resume_game():###
    global name, score, state, resume, money
    if os.path.exists(data_file):
        game_file = open(data_file, "r")
        info = game_file.read()
        if info == "":
            print("Empty File Cannot Resume")
            return
        else:
            name = input("Please Enter your Username: ")
    else:
        print("Cannot Resume No one has even played the game yet!")
        return
    load_game()
    print("\n" * 100)
    if ((name in game_data) and (game_data[name]["state"] == "True")):
        score = game_data[name]["score"]
        money = game_data[name]["money"]
        game_data[name]["state"] = "False"
        money = int(money)
        resume = True
        game()
        return
    else:
        print("\n" * 100)
        print("Game is not paused for this username")
        return

def game():
    global score, state, money
    cups = {"A": 1, "B": 2, "C": 3, "D": "PAUSE"}
    state = "False"
    visual = ("""                                                        
                    -#################+.                                    -#################+.                                    -#################+.                
              +#############################+                         +#############################+                         +#############################+           
           ############.-----------.############                   ############.-----------.############                   ############.-----------.############        
         -######-------..         ..-------######-               -######-------..         ..-------######-               -######-------..         ..-------######-      
         ####.--..                       ..--.####               ####.--..                       ..--.####               ####.--..                       ..--.####      
         ###-..                             ..-###               ###-..                             ..-###               ###-..                             ..-###      
         ##.--..                           ..--.##               ##.--..                           ..--.##               ##.--..                           ..--.##      
         ##-..----..                   ..----..-##               ##-..----..                   ..----..-##               ##-..----..                   ..----..-##      
         ##---....-----------------------....---##               ##---....-----------------------....---##               ##---....-----------------------....---##      
         ##-.-----..      ........     ..-----.-##               ##-.-----..      ........     ..-----.-##               ##-.-----..      ........     ..-----.-##      
        .##-    ..-----------------------..    -##.             .##-    ..-----------------------..    -##.             .##-    ..-----------------------..    -##.     
        ###-             .........             -##+             ###-             .........             -##+             ###-             .........             -##+     
        ###.                                   .###             ###.                                   .###             ###.                                   .###     
        ###.                                   .###             ###.                                   .###             ###.                                   .###     
        ##.                  ##                 .##             ##.           ############              .##             ##.                #########            .##     
        ##-                 #  #                -##             ##-           #           #             -##             ##-               #         #           -##     
       .##-                #    #               -##.           .##-           #            #            -##.           .##-              #                      -##.    
       ###.               #      #              .###           ###.           #             #           .###           ###.              #                      .###    
       ###.              #        #             .###           ###.           #            #            .###           ###.              #                      .###    
       ###.             #          #            .###           ###.           ############              .###           ###.              #                      .###    
       ##+             ##############            +##           ##+            #           #              +##           ##+               #                       +##    
       ##-            #              #           .##           ##-            #            #             .##           ##-               #                       .##    
       ##-           #                #          -##           ##-            #             #            -##           ##-               #                       -##    
      -##-          #                  #         -##-         -##-            #            #             -##-         -##-                #         #            -##-   
      ###-         #                    #        -###         ###-            #############              -###         ###-                 #########             -###   
      ###.                                       .###         ###.                                       .###         ###.                                       .###   
     .##-.                                       .-##        .##-.                                       .-##        .##-.                                       .-##   
     ###-                                         -###       ###-                                         -###       ###-                                         -###  
     ###-                                         -###.      ###-                                         -###.      ###-                                         -###. 
    -##--..                                     ..--##+     -##--..                                     ..--##+     -##--..                                     ..--##+ 
    ###-..--..                               ..--..-###     ###-..--..                               ..--..-###     ###-..--..                               ..--..-### 
    ###.......---..                     ..---.......###     ###.......---..                     ..---.......###     ###.......---..                     ..---.......### 
    ###. .--... .....-----------------.........--. .###     ###. .--... .....-----------------.........--. .###     ###. .--... .....-----------------.........--. .### 
    ###..    .---.....               .....---.    ..###     ###..    .---.....               .....---.    ..###     ###..    .---.....               .....---.    ..### 
    -###..         ..-----------------..         ..###-     -###..         ..-----------------..         ..###-     -###..         ..-----------------..         ..###- 
     #####..                                   ..#####       #####..                                   ..#####       #####..                                   ..#####  
      #######..                             ..#######         #######..                             ..#######         #######..                             ..#######   
        ########--.                     .-+########             ########--.                     .-+########             ########--.                     .-+########     
          -############------.------############-                 -############------.------############-                 -############------.------############-       
              +#############################+                         +#############################+                         +#############################+           
                   .+#################-.                                   .+#################-.                                   .+#################-.                
                                                       
                                                        """)
    print(visual)
    if resume == True:
        print(f"Resuming game for {name}\nCurrent Earning: {score}")
    print(f"Your Earning are currently: {score}\nYour Wallet Value are currently: {money}")
    invalidselection = False
    while money >= 5:
        random_cup = random.randint(1,3)
        guess = input("Please Choose Which Cup the Ball is IN :\nA.) CUP A\nB.) CUP B\nC.) CUP C\nD.) Pause\nEnter Selection Here: ").upper()
        if guess not in cups or guess == "":    
            print("\n" * 100)
            invalidselection = True
        elif cups[guess] == "PAUSE":
            state = "True"
            save_game()
            print("\n" * 100)
            print("Game paused. You can resume later.")
            return
        elif cups[guess] == random_cup:
            print("Wow! Nice guess!")
            score += 5
            money += 5
        else:
            print("\n" * 100)
            if random_cup == 1:
                ballcup = "A"
            elif random_cup == 2:
                ballcup = "B"
            elif random_cup == 3:
                ballcup = "C"
            money += -5
            print(f"Sorry, the ball was in Cup {ballcup}.")
            delay = input("Press Enter to Continue")
        print("\n" * 100)
        print(visual)
        if invalidselection == True:
            print("Not a valid selection. Please try again!")
        invalidselection = False
        print(f"Your Earning are currently: {score}\nYour Wallet Value are currently: {money}")
    save_game()
    show_leaderboard()

def save_game():
    load_game()
    game_data[name] = {"score": score, "state": state, "money": money}
    game_file = open(data_file, "w")
    for user in game_data:
        data = game_data[user]
        game_file.write(f"{user},{data["score"]},{data["state"]},{data["money"]}\n")
    game_file.close()
    hscore_save_game()

def load_game():
    if os.path.exists(data_file):
        game_file = open(data_file, "r")
        info = game_file.read()
        if info == "":
            return
        lines = info.split("\n")
        for line in lines:
            if line != "":
                name, score, state, money = line.split(",")
                game_data[name] = {"score": int(score), "state": state, "money": money} 
        game_file.close()

def hscore_save_game():
    hscore_load_game()
    if name not in hscore_data or score > hscore_data[name]["score"]:
        hscore_data[name] = {"score": score}
    game_file = open(hscore_file, "w")
    for user in hscore_data:
        data = hscore_data[user]
        game_file.write(f"{user},{data["score"]}\n")
    game_file.close()

def hscore_load_game():
    if os.path.exists(hscore_file):
        game_file = open(hscore_file, "r")
        info = game_file.read()
        if info == "":  
            return
        lines = info.split("\n")
        for line in lines:
            if line != "":
                name, score = line.split(",")
                hscore_data[name] = {"score": int(score)}
        game_file.close()

def show_leaderboard():
    if not os.path.exists(hscore_file):
        print("No Earnings found")
        return
    elif os.path.exists(hscore_file):
        game_file = open(hscore_file, "r")
        info = game_file.read()
        if info == "":
            print("No Earnings found")
            game_file.close
            return
        print("\n" * 100)
        print("Highest Earnings:")
        lines = info.split("\n")
        for line in lines:
            if line != "":
                name, score = line.split(",")
                print(f"{name}: {score}")
        game_file.close()
        delay = input("Press Enter Key to Return to Main Menu!")
        print("\n" * 100)
if __name__ == "__main__":
    menu()
