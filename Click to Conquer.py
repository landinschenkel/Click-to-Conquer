import time, random

inventory_list = []
player_weapon_list = ["Starter Sword", "Shadowfang Dagger", "Stormbringer Sword", "Frostbite Axe", "Nightmare Scythe", "Inferno Scepter", "Savage Claws"]
player_weapon_list_dictionary = {0: "A well-used, basic sword with a slightly worn hilt and blade. \nIt shows of numerous battles and has become a reliable, through unremarkable, weapon for an adventurer.",
                          1: "A small, sleek dagger forged from obsidian, emitting afaint dark glow. \nThe blade is lightweight and perfect for quick, stalthy attacks.",
                          2: "A large, fearsome sword crackling with electrical energy. \nThe blade hums with power, ready to unleash a devastating strike at any moment.",
                          3: "A massive axe with a blade covered in frost. \nThe weapon exudes a chilling aura, capable of freezing anything it touches.",
                          4: "A haunting scythe with a long, curved blade that seems to shimmer in and out of existence. \nThe weapon is said to steal the very essence of its victims.",
                          5: "A scepter crowned with a blazing crystal taht burns with an unquenchable fire. \nThe air around it ripples with heat, ready to incinerate foes.",
                          6: "Ferocious claws that extend from gauntlets, each talon sharpened to deadly point. \nThe wearer feels a surge of primal energy when they strike."}
monster_inventory = []
monster_weapon_list = ["Standard Sword", "Poisonous Fang", "Inverno Claw", "Shadow Spear", "Thunder Whip", "Ice Shard"]
player_hearts_list = ["♥"*20] 
monster_hearts_list = ["♥"*20]

def main():
    print("Hello, and welcome to my program!")
    choice = play_game()
    while True:
        if choice == "1":
            choice = floor_one()
        elif choice == "2":
            choice = floor_two()
        elif choice == "3":
            choice = floor_three()
        elif choice == "4":
            choice = floor_four()
        elif choice == "5":
            choice = floor_five()
        elif choice == "6":
            choice = floor_six()
        elif choice == "7":
            choice = last_floor()
        else:
            break
    print("Thanks for playing!\nGOODBYE!")

def play_game():
    print("""
    Hello and welcome to my Dungeon Game!
    You will start on the first floor of a ominous tower.
    For each floor you will have to defeat a certain monster in order to pass to the next floor.
    After defeating the monster you will be granted a chest which has a special item in it for you!
    Type 'Q' to end the program.
    Type 'S' to start the game!""")
    while True:
        choice = input("Enter your choice\n>> ").upper()
        if choice in ["S", " S", " S ", "s", " s", " s ",
                      "Q", " Q", " Q ", "q", " q", " q "]:
            break
        else:
            print("Please enter a valid choice: 'S' or 'Q'\n")
    if choice == "S":
        return "1"
    else:
        return "Q"
    
def print_room_header(room):
    print("\n"*4)
    line = '=' * 25
    print(f"\n{line}{room}{line}")

def floor_one():
    global monster_weapon, monster_inventory, monster_die, player_die, choice, weapon, w, monster_hearts_list, player_hearts_list, player_weapon_list, player_weapon_list_dictionary, monster_weapon_list
    print_room_header("First FLoor")
    print("----------------------------------------------------------")
    print("|                                                        |")
    print("|                                                        |")
    print("|                      _____________                     |")
    print("|                    / -----\\ /----- \\                   |")
    print("|                   |        0        |                  |")
    print("|                   |                 |                  |")
    print("|                   |                 |                  |")
    print("|                   |                 |                  |")
    print("|                    \\_______________/                   |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                            O                           |")
    print("|                           /|\\                          |")
    print("|                           / \\                          |")
    print("|                 ",player_hearts_list[0],"                 |")
    print("|                                                        |")
    print("|                                                        |")
    print("----------------------------------------------------------")
    print("""
        \n\nYou are on the first floor of the terrifying tower.
        There are no windows at all in the tower. And there is barely any light in the room.
        There are only a few candles scattered on the floor. Barely lighting up the room.  
        But with that being said... there is an giant chest in the middle of the room.
        Press 'N' to open the chest
        Press 'Q' to quit the game\n""")
    while True:
        choice = input("Enter your choice\n>> ").upper()
        if choice in ["N", " N", " N ",
                      "Q", " Q", " Q "]:
            break
        else:
            print("Please enter a valid choice\n")
    if choice in ["N", " N", " N "]:
        print("\n\nThe second you open the chest you recived: ", player_weapon_list_dictionary[0], " And you automatically teleported to the first challenge.")
        inventory_list.append(player_weapon_list[0])
        return "2"
    else:
        return "Q"

def floor_two():
    global monster_weapon, monster_inventory, monster_die, player_die, choice, weapon, w, monster_hearts_list, player_hearts_list, player_weapon_list, player_weapon_list_dictionary, monster_weapon_list
    print_room_header("First Challenge")
    print("----------------------------------------------------------")
    print("|                                                        |")
    print("|                                                        |")
    print("|                       , / | \\                          |")
    print("|                    ( '        ' )                      |")
    print("|                      \\  | ^ |  /                       |")
    print("|                         /   \\                          |")
    print("|                ",monster_hearts_list[0],"                  |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                            O                           |")
    print("|                           /|\\                          |")
    print("|                           / \\                          |")
    print("|                 ",player_hearts_list[0],"                 |")
    print("|                                                        |")
    print("|                                                        |")
    print("----------------------------------------------------------")
    print("""
        \n\n
        You are in the first challenge of the terrifying tower.
        There are no windows at all in the tower. And there is barely any light in the room.
        There are only a few candles scattered on the floor. Barely lighting up the room.
        But with that being said... there is an giant Orc in the middle of the room.
        Press 'F' to fight the Orc
        Press 'Q' to quit the game\n""")
    while True:
        choice = input("Enter your choice\n>> ").upper()
        if choice in ["F", " F", " F ",
                      "Q", " Q", " Q "]:
            break
        else:
            print("Please enter a valid choice\n")
    if choice in ["F", " F", " F "]:
        while len(monster_hearts_list[0]) > 0 and len(player_hearts_list[0]) > 0:
            player_die = random.randint(1, 2)
            print("\n" * 20)
            print("\nSo you decided to fight the Orc.. You roll a dice.. and it was a ", player_die, " that means you did ", player_die, " damage!")
            monster_hearts_list[0] = monster_hearts_list[0][:-player_die]

            print("\n\n\n\n")
            print("----------------------------------------------------------")
            print("|                                                        |")
            print("|                                                        |")
            print("|                       , / | \\                          |")
            print("|                    ( '        ' )                      |")
            print("|                      \\  | ^ |  /                       |")
            print("|                         /   \\                          |")
            print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                            O                           |")
            print("|                           /|\\                          |")
            print("|                           / \\                          |")
            print("|                 ",player_hearts_list[0],"                 |")
            print("|                                                        |")
            print("|                                                        |")
            print("----------------------------------------------------------")
            time.sleep(5)
            if len(monster_hearts_list[0]) > 0:
                monster_die = random.randint(0, 2)
                print("It is now the Orcs turn.. and it does ", monster_die, " to you!")
                if monster_die > 0:
                    player_hearts_list[0] = player_hearts_list[0][:-monster_die]

                print("\n\n\n\n")
                print("----------------------------------------------------------")
                print("|                                                        |")
                print("|                                                        |")
                print("|                       , / | \\                          |")
                print("|                    ( '        ' )                      |")
                print("|                      \\  | ^ |  /                       |")
                print("|                         /   \\                          |")
                print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                            O                           |")
                print("|                           /|\\                          |")
                print("|                           / \\                          |")
                print("|                 ",player_hearts_list[0],"                 |")
                print("|                                                        |")
                print("|                                                        |")
                print("----------------------------------------------------------")
                time.sleep(5)

        if len(monster_hearts_list[0]) <= 0:
            print("You defeated the Orc!")
            print("----------------------------------------------------------")
            print("|                                                        |")
            print("|                                                        |")
            print("|                      _____________                     |")
            print("|                    / -----\\ /----- \\                   |")
            print("|                   |        0        |                  |")
            print("|                   |                 |                  |")
            print("|                   |                 |                  |")
            print("|                   |                 |                  |")
            print("|                    \\_______________/                   |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                            O                           |")
            print("|                           /|\\                          |")
            print("|                           / \\                          |")
            print("|                 ",player_hearts_list[0],"                 |")
            print("|                                                        |")
            print("|                                                        |")
            print("----------------------------------------------------------")
            print("""
                \n\nYou have defeated the Orc! And the very second you killed the orc \
                a chest spawned right where the Orc was. What ever will be inside??
                Press 'N' to open the chest
                Press 'Q' to quit the game\n""")
            while True:
                choice = input("Enter your choice\n>> ").upper()
                if choice in ["N", " N", " N ",
                            "Q", " Q", " Q "]:
                    break
                else:
                    print("Please enter a valid choice\n")
            if choice in ["N", " N", " N "]:
                inventory_list = []
                length_weapon_list = len(player_weapon_list)
                w = random.randint(1, length_weapon_list)
                print("\n\nThe second you open the chest you recived: ", player_weapon_list_dictionary[w], " And you automatically teleported to the first challenge.")
                inventory_list.append(player_weapon_list[w])
                del player_weapon_list_dictionary[w]
                player_weapon_list.remove(w)
                if inventory_list[0] == "Shadowfang Dagger":
                    weapon = "Shadowfang Dagger"
                elif inventory_list[0] == "Stormbringer Sword":
                    weapon = "Stormbringer Sword"
                elif inventory_list[0] == "Frostbite Axe":
                    weapon = "Frostbite Axe"
                elif inventory_list[0] == "Nightmare Scythe":
                    weapon = "Nightmare Scythe"
                elif inventory_list[0] == "Inferno Scepter":
                    weapon = "Inferno Scepter"
                else:
                    weapon = "Savage Claws"
                monster_inventory = []
                length_weapon_list = len(player_weapon_list)
                w = random.randint(0, length_weapon_list)
                monster_inventory.append(monster_weapon_list[w])
                monster_weapon_list.remove(w)
                if monster_inventory[0] == "Standard Sword":
                    monster_weapon = "Standard Sword"
                elif monster_inventory[0] == "Poisonous Fang":
                    monster_weapon = "Poisonous Fang"
                elif monster_inventory[0] == "Inferno Claw":
                    monster_weapon = "Inferno Claw"
                elif monster_inventory[0] == "Shadow Spear":
                    monster_weapon = "Shadow Spear"
                elif monster_inventory[0] == "Thunder Whip":
                    monster_weapon = "Thunder Whip"
                elif monster_inventory[0] == "Ice Shard":
                    monster_weapon = "Ice Shard"

                return "3"
            else:
                return "Q"
        if len(player_hearts_list[0]) <= 0:
            print("You were defeated by the Orc...")
            print("""
 _____  ____   _       _____   ____   _      _____  ____ 
/  __/ /  _ \\ / \\__/| /  __/  /  _ \\ / \\ |\\ /  __/ /  __\\ 
| |  _ | / \\| | |\\/|| |  \\    | / \\| | | // |  \\   |  \\/|
| |_// | |-|| | |  || |  /_   | \\_/| | \\//  |  /_  |    /
\\____\\ \\_/ \\| \\_/  \\| \\____\\  \\____/ \\__/   \\____\\ \\_/\\_\\ 
                                                   """)
            return "1"
    else:
        return "Q"
    
def floor_three():
    global monster_weapon, monster_inventory, monster_die, player_die, choice, weapon, w, monster_hearts_list, player_hearts_list, player_weapon_list, player_weapon_list_dictionary, monster_weapon_list
    print_room_header("Second Challenge")
    print("----------------------------------------------------------")
    print("|                                                        |")
    print("|                                                        |")
    print("|                      ____       __                     |")
    print("|                     |    \\    /    |                   |")
    print("|                      \\  ( O O )  /                     |")
    print("|                       |    u    |                      |")
    print("|                       > - ^ ^ - <                      |")
    print("|                       > - v v - <                      |")
    print("|                ",player_hearts_list[0],"                  |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                            O                           |")
    print("|                           /|\\                          |")
    print("|                           / \\                          |")
    print("|                 ",player_hearts_list[0],"                 |")
    print("|                                                        |")
    print("|                                                        |")
    print("----------------------------------------------------------")
    print("""
        \n\nYou are in the Second challenge of the terrifying tower.
        There are no windows at all in the tower. And there is barely any light in the room.
        There are only a few candles scattered on the floor. Barely lighting up the room.
        But with that being said... there is an giant Evil Bunny in the middle of the room.
        Press 'F' to fight the Evil Bunny
        Press 'Q' to quit the game\n""")
    while True:
        choice = input("Enter your choice\n>> ").upper()
        if choice in ["F", " F", " F ",
                      "Q", " Q", " Q "]:
            break
        else:
            print("Please enter a valid choice\n")
    if choice in ["F", " F", " F "]:
        while len(monster_hearts_list[0]) > 0 and len(player_hearts_list[0]) > 0:
            if weapon == "Shadowfang Dagger":
                player_die = random.randint(2, 5)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                stun_roll = random.randint(1, 10)
                if stun_roll % 2 == 0:
                    print(f"\nThe Shadowfang Dagger stuns the Evil Bunny with a roll of {stun_roll}!")
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Stormbringer Sword":
                player_die = random.randint(5, 10)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                paralyze_roll = random.randint(1, 4)
                if paralyze_roll == 1:
                    print(f"\nThe Stormbringer Sword strikes the Evil Bunny with a bolt of lightning and paralyzes it with a roll of {paralyze_roll}!")
                    player_die += 1
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Frostbite Axe":
                player_die = random.randint(6, 9)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                freeze_roll = random.randint(1, 2)
                if freeze_roll == 2:
                    print(f"\nThe Frostbite Axe freezes the Evil Bunny with a roll of {freeze_roll}!")
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("\n\n\n\n")
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Nightmare Scythe":
                player_die = random.randint(5, 10)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                sleep_roll = random.randint(1, 2)
                if sleep_roll % 2 == 0:
                    print(f"\nThe Nightmare Scythe puts the Evil Bunny to sleep with a roll of {sleep_roll}!")
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    time.sleep(5)
                    continue
            elif weapon == "Inferno Scepter":
                player_die = random.randint(3, 5)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                fire_roll = random.randint(1, 10)
                if fire_roll % 2 == 0:
                    print(f"\nThe Inferno Scepter strikes the Evil Potato with a rain of fire and deals an extra 1 damage with a roll of {fire_roll}!")
                    player_die += 1
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Savage Claws":
                player_die = random.randint(2, 5)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                print("----------------------------------------------------------")
                print("|                                                        |")
                print("|                                                        |")
                print("|                      ____       __                     |")
                print("|                     |    \\    /    |                   |")
                print("|                      \\  ( O O )  /                     |")
                print("|                       |    u    |                      |")
                print("|                       > - ^ ^ - <                      |")
                print("|                       > - v v - <                      |")
                print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                            O                           |")
                print("|                           /|\\                          |")
                print("|                           / \\                          |")
                print("|                 ",player_hearts_list[0],"                 |")
                print("|                                                        |")
                print("|                                                        |")
                print("----------------------------------------------------------")
                time.sleep(5)
                

                hearts_to_add = player_die
                for _ in range(hearts_to_add):
                    if len(player_hearts_list[0]) < 20:  # Assuming max health is 20 hearts
                        player_hearts_list[0] += "♥"
                    else:
                        break

            
            # Monster attacks
            if len(monster_hearts_list[0]) > 0:
                if monster_weapon == "Standard Sword":
                    monster_die = random.randint(0, 2)
                    if monster_die > 0:
                        player_hearts_list[0] = player_hearts_list[0][:-monster_die]
                elif monster_weapon == "Poisonous Fang":
                    monster_die = random.randint(2, 5)
                    poison_roll = random.randint(1, 5)
                    if poison_roll % 2 == 0:
                        monster_die += 1
                        print(f"\nThe Poisonous Fang poisons you meaning it does an extra 1 damage!")
                    if monster_die > 0:
                        player_hearts_list[0] = player_hearts_list[0][:-monster_die]
                elif monster_weapon == "Inferno Claw":
                    monster_die = random.randint(3, 7)
                    inferno_roll = random.randint(1, 4)
                    if inferno_roll % 2 == 0:
                        print(f"\nThe Inferno Claw sets you on fire dealing an extra 2 damage!")
                        monster_die += 2
                    if monster_die > 0:
                        player_hearts_list[0] = player_hearts_list[0][:-monster_die]
                elif monster_weapon == "Shadow Spear":
                    monster_die = random.randint(4, 6)
                    shadow_roll = random.randint(1, 2)
                    if shadow_roll == 2:
                        monster_die += 1
                        print(f"\nThe Shadow Spear deals 1 extra damage!")
                    if monster_die > 0:
                        player_hearts_list[0] = player_hearts_list[0][:-monster_die]
                elif monster_weapon == "Thunder Whip":
                    monster_die = random.randint(5, 10)
                    thunder_roll = random.randint(1, 9)
                    if thunder_roll == 1:
                        monster_die += 3
                        print(f"\nThe Thunder Whip deals 3 extra damage!")
                    if monster_die > 0:
                        player_hearts_list[0] = player_hearts_list[0][:-monster_die]
                elif monster_weapon == "Ice Shard":
                    monster_die = random.randint(2, 9)
                    ice_roll = random.randint(1, 10)
                    if ice_roll % 2 == 0:
                        monster_die += 1
                        print(f"\nThe Ice Shard deals 1 extra damage!")
                    if monster_die > 0:
                        player_hearts_list[0] = player_hearts_list[0][:-monster_die]

                print("\n\n\n\n")
                print("----------------------------------------------------------")
                print("|                                                        |")
                print("|                                                        |")
                print("|                      ____       __                     |")
                print("|                     |    \\    /    |                   |")
                print("|                      \\  ( O O )  /                     |")
                print("|                       |    u    |                      |")
                print("|                       > - ^ ^ - <                      |")
                print("|                       > - v v - <                      |")
                print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                            O                           |")
                print("|                           /|\\                          |")
                print("|                           / \\                          |")
                print("|                 ",player_hearts_list[0],"                 |")
                print("|                                                        |")
                print("|                                                        |")
                print("----------------------------------------------------------")
                time.sleep(5)
        if len(monster_hearts_list[0]) <= 0:
            print("You defeated the Evil Bunny!")
            print("----------------------------------------------------------")
            print("|                                                        |")
            print("|                                                        |")
            print("|                      _____________                     |")
            print("|                    / -----\\ /----- \\                   |")
            print("|                   |        0        |                  |")
            print("|                   |                 |                  |")
            print("|                   |                 |                  |")
            print("|                   |                 |                  |")
            print("|                    \\_______________/                   |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                            O                           |")
            print("|                           /|\\                          |")
            print("|                           / \\                          |")
            print("|                 ",player_hearts_list[0],"                 |")
            print("|                                                        |")
            print("|                                                        |")
            print("----------------------------------------------------------")
            print("""
                \n\nYou have defeated the Evil Bunny! And the very second you killed the Evil Bunny \
                a chest spawned right where the Evil Bunny was. What ever will be inside??
                Press 'N' to open the chest
                Press 'Q' to quit the game\n""")
            while True:
                choice = input("Enter your choice\n>> ").upper()
                if choice in ["N", " N", " N ",
                            "Q", " Q", " Q "]:
                    break
                else:
                    print("Please enter a valid choice\n")
            if choice in ["N", " N", " N "]:
                inventory_list = []
                length_weapon_list = len(player_weapon_list)
                w = random.randint(1, length_weapon_list)
                print("\n\nThe second you open the chest you recived: ", player_weapon_list_dictionary[w], " And you automatically teleported to the first challenge.")
                inventory_list.append(player_weapon_list[w])
                del player_weapon_list_dictionary[w]
                player_weapon_list.remove(w)
                if inventory_list[0] == "Shadowfang Dagger":
                    weapon = "Shadowfang Dagger"
                elif inventory_list[0] == "Stormbringer Sword":
                    weapon = "Stormbringer Sword"
                elif inventory_list[0] == "Frostbite Axe":
                    weapon = "Frostbite Axe"
                elif inventory_list[0] == "Nightmare Scythe":
                    weapon = "Nightmare Scythe"
                elif inventory_list[0] == "Inferno Scepter":
                    weapon = "Inferno Scepter"
                else:
                    weapon = "Savage Claws"
                monster_inventory = []
                length_weapon_list = len(player_weapon_list)
                w = random.randint(0, length_weapon_list)
                monster_inventory.append(monster_weapon_list[w])
                monster_weapon_list.remove(w)
                if monster_inventory[0] == "Standard Sword":
                    monster_weapon = "Standard Sword"
                elif monster_inventory[0] == "Poisonous Fang":
                    monster_weapon = "Poisonous Fang"
                elif monster_inventory[0] == "Inferno Claw":
                    monster_weapon = "Inferno Claw"
                elif monster_inventory[0] == "Shadow Spear":
                    monster_weapon = "Shadow Spear"
                elif monster_inventory[0] == "Thunder Whip":
                    monster_weapon = "Thunder Whip"
                elif monster_inventory[0] == "Ice Shard":
                    monster_weapon = "Ice Shard"
                return "4"
            else:
                return "Q"
        if len(player_hearts_list[0]) <= 0:
            print("You were defeated by the Evil Bunny...")
            print("""
 _____  ____   _       _____   ____   _      _____  ____ 
/  __/ /  _ \\ / \\__/| /  __/  /  _ \\ / \\ |\\ /  __/ /  __\\ 
| |  _ | / \\| | |\\/|| |  \\    | / \\| | | // |  \\   |  \\/|
| |_// | |-|| | |  || |  /_   | \\_/| | \\//  |  /_  |    /
\\____\\ \\_/ \\| \\_/  \\| \\____\\  \\____/ \\__/   \\____\\ \\_/\\_\\ 
                                                   """)
            return "1"
    else:
        return "Q"

def floor_four():
    global monster_weapon, monster_inventory, monster_die, player_die, choice, weapon, w, monster_hearts_list, player_hearts_list, player_weapon_list, player_weapon_list_dictionary, monster_weapon_list
    print_room_header("Challenge Three")
    print("----------------------------------------------------------")
    print("|                        _________                       |")
    print("|                       (         )                      |")
    print("|                      (           )                     |")
    print("|                {----(     oo      )----}               |")
    print("|                   (       ~        )                   |")
    print("|                  (__________________)                  |")
    print("|                                                        |")
    print("|                ",player_hearts_list[0],"                  |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                            O                           |")
    print("|                           /|\\                          |")
    print("|                           / \\                          |")
    print("|                 ",player_hearts_list[0],"                 |")
    print("|                                                        |")
    print("|                                                        |")
    print("----------------------------------------------------------")
    print("""
        \n\nYou are in the Third challenge of the terrifying tower.
        There are no windows at all in the tower. And there is barely any light in the room.
        There are only a few candles scattered on the floor. Barely lighting up the room.
        But with that being said... there is an giant Slime in the middle of the room.
        Press 'F' to fight the Slime
        Press 'Q' to quit the game\n""")
    while True:
        choice = input("Enter your choice\n>> ").upper()
        if choice in ["F", " F", " F ",
                      "Q", " Q", " Q "]:
            break
        else:
            print("Please enter a valid choice\n")
    if choice in ["F", " F", " F "]:
        while len(monster_hearts_list[0]) > 0 and len(player_hearts_list[0]) > 0:
            if weapon == "Shadowfang Dagger":
                player_die = random.randint(2, 5)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                stun_roll = random.randint(1, 10)
                if stun_roll % 2 == 0:
                    print(f"\nThe Shadowfang Dagger stuns the Evil Bunny with a roll of {stun_roll}!")
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Stormbringer Sword":
                player_die = random.randint(5, 10)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                paralyze_roll = random.randint(1, 4)
                if paralyze_roll == 1:
                    print(f"\nThe Stormbringer Sword strikes the Evil Bunny with a bolt of lightning and paralyzes it with a roll of {paralyze_roll}!")
                    player_die += 1
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Frostbite Axe":
                player_die = random.randint(6, 9)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                freeze_roll = random.randint(1, 2)
                if freeze_roll == 2:
                    print(f"\nThe Frostbite Axe freezes the Evil Bunny with a roll of {freeze_roll}!")
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("\n\n\n\n")
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Nightmare Scythe":
                player_die = random.randint(5, 10)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                sleep_roll = random.randint(1, 2)
                if sleep_roll % 2 == 0:
                    print(f"\nThe Nightmare Scythe puts the Evil Bunny to sleep with a roll of {sleep_roll}!")
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    time.sleep(5)
                    continue
            elif weapon == "Inferno Scepter":
                player_die = random.randint(3, 5)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                fire_roll = random.randint(1, 10)
                if fire_roll % 2 == 0:
                    print(f"\nThe Inferno Scepter strikes the Evil Potato with a rain of fire and deals an extra 1 damage with a roll of {fire_roll}!")
                    player_die += 1
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Savage Claws":
                player_die = random.randint(2, 5)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                print("----------------------------------------------------------")
                print("|                                                        |")
                print("|                                                        |")
                print("|                      ____       __                     |")
                print("|                     |    \\    /    |                   |")
                print("|                      \\  ( O O )  /                     |")
                print("|                       |    u    |                      |")
                print("|                       > - ^ ^ - <                      |")
                print("|                       > - v v - <                      |")
                print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                            O                           |")
                print("|                           /|\\                          |")
                print("|                           / \\                          |")
                print("|                 ",player_hearts_list[0],"                 |")
                print("|                                                        |")
                print("|                                                        |")
                print("----------------------------------------------------------")
                time.sleep(5)
                

                hearts_to_add = player_die
                for _ in range(hearts_to_add):
                    if len(player_hearts_list[0]) < 20:  # Assuming max health is 20 hearts
                        player_hearts_list[0] += "♥"
                    else:
                        break
            if len(monster_hearts_list[0]) > 0:
                if monster_weapon == "Standard Sword":
                    monster_die = random.randint(0, 2)
                    for _ in range(monster_die):
                        if player_hearts_list[0]:
                            player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Poisonous Fang":
                    monster_die = random.randint(2, 5)
                    poison_roll = random.randint(1, 5)
                    if poison_roll % 2 == 0:
                        monster_die += 1
                        print(f"\nThe Poisonous Fang poisons you meaning it does an extra 1 damage!")
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Inferno Claw":
                    monster_die = random.randint(3, 7)
                    inferno_roll = random.randint(1, 4)
                    if inferno_roll % 2 == 0:
                        print(f"\nThe Inferno Claw sets you on fire dealing an extra 2 damage!")
                        monster_die += 2
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Shadow Spear":
                    monster_die = random.randint(4, 6)
                    shadow_roll = random.randint(1, 2)
                    if shadow_roll == 2:
                        monster_die += 1
                        print(f"\nThe Shadow Spear deals 1 extra damage!")
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Thunder Whip":
                    monster_die = random.randint(5, 10)
                    thunder_roll = random.randint(1, 9)
                    if thunder_roll == 1:
                        monster_die += 3
                        print(f"\nThe Thunder Whip deals 3 extra damage!")
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Ice Shard":
                    monster_die = random.randint(2, 9)
                    ice_roll = random.randint(1, 10)
                    if ice_roll % 2 == 0:
                        monster_die += 1
                        print(f"\nThe Ice Shard deals 1 extra damage!")
                        monster_die += 1
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                print("\n\n\n\n")
                print("----------------------------------------------------------")
                print("|                        _________                       |")
                print("|                       (         )                      |")
                print("|                      (           )                     |")
                print("|                {----(     oo      )----}               |")
                print("|                   (       ~        )                   |")
                print("|                  (__________________)                  |")
                print("|                                                        |")
                print("|                ", "".join(monster_hearts_list),"                  |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                            O                           |")
                print("|                           /|\\                          |")
                print("|                           / \\                          |")
                print("|                 ",player_hearts_list[0],"                 |")
                print("|                                                        |")
                print("|                                                        |")
                print("----------------------------------------------------------")
                time.sleep(5)
        if len(monster_hearts_list[0]) <= 0:
            print("You defeated the Slime!")
            print("----------------------------------------------------------")
            print("|                                                        |")
            print("|                                                        |")
            print("|                      _____________                     |")
            print("|                    / -----\\ /----- \\                   |")
            print("|                   |        0        |                  |")
            print("|                   |                 |                  |")
            print("|                   |                 |                  |")
            print("|                   |                 |                  |")
            print("|                    \\_______________/                   |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                            O                           |")
            print("|                           /|\\                          |")
            print("|                           / \\                          |")
            print("|                 ",player_hearts_list[0],"                 |")
            print("|                                                        |")
            print("|                                                        |")
            print("----------------------------------------------------------")
            print("""
                \n\nYou have defeated the Slime! And the very second you killed the Slime \
                a chest spawned right where the Slime was. What ever will be inside??
                Press 'N' to open the chest
                Press 'Q' to quit the game\n""")
            while True:
                choice = input("Enter your choice\n>> ").upper()
                if choice in ["N", " N", " N ",
                            "Q", " Q", " Q "]:
                    break
                else:
                    print("Please enter a valid choice\n")
            if choice in ["N", " N", " N "]:
                inventory_list = []
                length_weapon_list = len(player_weapon_list)
                w = random.randint(1, length_weapon_list)
                print("\n\nThe second you open the chest you recived: ", player_weapon_list_dictionary[w], " And you automatically teleported to the first challenge.")
                inventory_list.append(player_weapon_list[w])
                del player_weapon_list_dictionary[w]
                player_weapon_list.remove(player_weapon_list[w])
                if inventory_list[0] == "Shadowfang Dagger":
                    weapon = "Shadowfang Dagger"
                elif inventory_list[0] == "Stormbringer Sword":
                    weapon = "Stormbringer Sword"
                elif inventory_list[0] == "Frostbite Axe":
                    weapon = "Frostbite Axe"
                elif inventory_list[0] == "Nightmare Scythe":
                    weapon = "Nightmare Scythe"
                elif inventory_list[0] == "Inferno Scepter":
                    weapon = "Inferno Scepter"
                else:
                    weapon = "Savage Claws"
                monster_inventory = []
                length_weapon_list = len(player_weapon_list)
                w = random.randint(0, length_weapon_list - 1)
                monster_inventory.append(monster_weapon_list[w])
                monster_weapon_list.remove(monster_weapon_list[w])
                if monster_inventory[0] == "Standard Sword":
                    monster_weapon = "Standard Sword"
                elif monster_inventory[0] == "Poisonous Fang":
                    monster_weapon = "Poisonous Fang"
                elif monster_inventory[0] == "Inferno Claw":
                    monster_weapon = "Inferno Claw"
                elif monster_inventory[0] == "Shadow Spear":
                    monster_weapon = "Shadow Spear"
                elif monster_inventory[0] == "Thunder Whip":
                    monster_weapon = "Thunder Whip"
                elif monster_inventory[0] == "Ice Shard":
                    monster_weapon = "Ice Shard"
                return "5"
            else:
                return "Q"
        if len(player_hearts_list[0]) <= 0:
            print("You were defeated by the Slime...")
            print("""
 _____  ____   _       _____   ____   _      _____  ____ 
/  __/ /  _ \\ / \\__/| /  __/  /  _ \\ / \\ |\\ /  __/ /  __\\ 
| |  _ | / \\| | |\\/|| |  \\    | / \\| | | // |  \\   |  \\/|
| |_// | |-|| | |  || |  /_   | \\_/| | \\//  |  /_  |    /
\\____\\ \\_/ \\| \\_/  \\| \\____\\  \\____/ \\__/   \\____\\ \\_/\\_\\ 
                                                   """)
            return "1"
    else:
        return "Q"

def floor_five():
    global monster_weapon, monster_inventory, monster_die, player_die, choice, weapon, w, monster_hearts_list, player_hearts_list, player_weapon_list, player_weapon_list_dictionary, monster_weapon_list
    print_room_header("Challenge Four")
    print("----------------------------------------------------------")
    print("|                        _    _                          |")
    print("|                       / \\__/ \\                         |")
    print("|                      {  0  0  }                        |")
    print("|                        (  ~ )                          |")
    print("|                         |  | \\                         |")
    print("|                                                        |")
    print("|                ",player_hearts_list[0],"                  |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                            O                           |")
    print("|                           /|\\                          |")
    print("|                           / \\                          |")
    print("|                 ",player_hearts_list[0],"                 |")
    print("|                                                        |")
    print("|                                                        |")
    print("----------------------------------------------------------")
    print("""
        \n\nYou are in the Fourth challenge of the terrifying tower.
        There are no windows at all in the tower. And there is barely any light in the room.
        There are only a few candles scattered on the floor. Barely lighting up the room.
        But with that being said... there is an giant Cat in the middle of the room.
        Press 'F' to fight the Evil Cat
        Press 'Q' to quit the game\n""")
    while True:
        choice = input("Enter your choice\n>> ").upper()
        if choice in ["F", " F", " F ",
                      "Q", " Q", " Q "]:
            break
        else:
            print("Please enter a valid choice\n")
    if choice in ["F", " F", " F "]:
        while len(monster_hearts_list[0]) > 0 and len(player_hearts_list[0]) > 0:
            if weapon == "Shadowfang Dagger":
                player_die = random.randint(2, 5)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                stun_roll = random.randint(1, 10)
                if stun_roll % 2 == 0:
                    print(f"\nThe Shadowfang Dagger stuns the Evil Bunny with a roll of {stun_roll}!")
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Stormbringer Sword":
                player_die = random.randint(5, 10)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                paralyze_roll = random.randint(1, 4)
                if paralyze_roll == 1:
                    print(f"\nThe Stormbringer Sword strikes the Evil Bunny with a bolt of lightning and paralyzes it with a roll of {paralyze_roll}!")
                    player_die += 1
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Frostbite Axe":
                player_die = random.randint(6, 9)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                freeze_roll = random.randint(1, 2)
                if freeze_roll == 2:
                    print(f"\nThe Frostbite Axe freezes the Evil Bunny with a roll of {freeze_roll}!")
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("\n\n\n\n")
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Nightmare Scythe":
                player_die = random.randint(5, 10)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                sleep_roll = random.randint(1, 2)
                if sleep_roll % 2 == 0:
                    print(f"\nThe Nightmare Scythe puts the Evil Bunny to sleep with a roll of {sleep_roll}!")
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    time.sleep(5)
                    continue
            elif weapon == "Inferno Scepter":
                player_die = random.randint(3, 5)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                fire_roll = random.randint(1, 10)
                if fire_roll % 2 == 0:
                    print(f"\nThe Inferno Scepter strikes the Evil Potato with a rain of fire and deals an extra 1 damage with a roll of {fire_roll}!")
                    player_die += 1
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Savage Claws":
                player_die = random.randint(2, 5)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                print("----------------------------------------------------------")
                print("|                                                        |")
                print("|                                                        |")
                print("|                      ____       __                     |")
                print("|                     |    \\    /    |                   |")
                print("|                      \\  ( O O )  /                     |")
                print("|                       |    u    |                      |")
                print("|                       > - ^ ^ - <                      |")
                print("|                       > - v v - <                      |")
                print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                            O                           |")
                print("|                           /|\\                          |")
                print("|                           / \\                          |")
                print("|                 ",player_hearts_list[0],"                 |")
                print("|                                                        |")
                print("|                                                        |")
                print("----------------------------------------------------------")
                time.sleep(5)
                

                hearts_to_add = player_die
                for _ in range(hearts_to_add):
                    if len(player_hearts_list[0]) < 20:  # Assuming max health is 20 hearts
                        player_hearts_list[0] += "♥"
                    else:
                        break
            if len(monster_hearts_list[0]) > 0:
                if monster_weapon == "Standard Sword":
                    monster_die = random.randint(0, 2)
                    for _ in range(monster_die):
                        if player_hearts_list[0]:
                            player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Poisonous Fang":
                    monster_die = random.randint(2, 5)
                    poison_roll = random.randint(1, 5)
                    if poison_roll % 2 == 0:
                        monster_die += 1
                        print(f"\nThe Poisonous Fang poisons you meaning it does an extra 1 damage!")
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Inferno Claw":
                    monster_die = random.randint(3, 7)
                    inferno_roll = random.randint(1, 4)
                    if inferno_roll % 2 == 0:
                        print(f"\nThe Inferno Claw sets you on fire dealing an extra 2 damage!")
                        monster_die += 2
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Shadow Spear":
                    monster_die = random.randint(4, 6)
                    shadow_roll = random.randint(1, 2)
                    if shadow_roll == 2:
                        monster_die += 1
                        print(f"\nThe Shadow Spear deals 1 extra damage!")
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Thunder Whip":
                    monster_die = random.randint(5, 10)
                    thunder_roll = random.randint(1, 9)
                    if thunder_roll == 1:
                        monster_die += 3
                        print(f"\nThe Thunder Whip deals 3 extra damage!")
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Ice Shard":
                    monster_die = random.randint(2, 9)
                    ice_roll = random.randint(1, 10)
                    if ice_roll % 2 == 0:
                        monster_die += 1
                        print(f"\nThe Ice Shard deals 1 extra damage!")
                        monster_die += 1
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                print("\n\n\n\n")
                print("----------------------------------------------------------")
                print("|                        _    _                          |")
                print("|                       / \\__/ \\                         |")
                print("|                      {  0  0  }                        |")
                print("|                        (  ~ )                          |")
                print("|                         |  | \\                         |")
                print("|                                                        |")
                print("|                ", "".join(monster_hearts_list),"                  |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                            O                           |")
                print("|                           /|\\                          |")
                print("|                           / \\                          |")
                print("|                 ",player_hearts_list[0],"                 |")
                print("|                                                        |")
                print("|                                                        |")
                print("----------------------------------------------------------")
                time.sleep(5)
        if len(monster_hearts_list[0]) <= 0:
            print("You defeated the Cat!")
            print("----------------------------------------------------------")
            print("|                                                        |")
            print("|                                                        |")
            print("|                      _____________                     |")
            print("|                    / -----\\ /----- \\                   |")
            print("|                   |        0        |                  |")
            print("|                   |                 |                  |")
            print("|                   |                 |                  |")
            print("|                   |                 |                  |")
            print("|                    \\_______________/                   |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                            O                           |")
            print("|                           /|\\                          |")
            print("|                           / \\                          |")
            print("|                 ",player_hearts_list[0],"                 |")
            print("|                                                        |")
            print("|                                                        |")
            print("----------------------------------------------------------")
            print("""
                \n\nYou have defeated the Slime! And the very second you killed the Cat \
                a chest spawned right where the Cat was. What ever will be inside??
                Press 'N' to open the chest
                Press 'Q' to quit the game\n""")
            while True:
                choice = input("Enter your choice\n>> ").upper()
                if choice in ["N", " N", " N ",
                            "Q", " Q", " Q "]:
                    break
                else:
                    print("Please enter a valid choice\n")
            if choice in ["N", " N", " N "]:
                inventory_list = []
                length_weapon_list = len(player_weapon_list)
                w = random.randint(1, length_weapon_list)
                print("\n\nThe second you open the chest you recived: ", player_weapon_list_dictionary[w], " And you automatically teleported to the fith challenge.")
                inventory_list.append(player_weapon_list[w])
                del player_weapon_list_dictionary[w]
                player_weapon_list.remove(w)
                if inventory_list[0] == "Shadowfang Dagger":
                    weapon = "Shadowfang Dagger"
                elif inventory_list[0] == "Stormbringer Sword":
                    weapon = "Stormbringer Sword"
                elif inventory_list[0] == "Frostbite Axe":
                    weapon = "Frostbite Axe"
                elif inventory_list[0] == "Nightmare Scythe":
                    weapon = "Nightmare Scythe"
                elif inventory_list[0] == "Inferno Scepter":
                    weapon = "Inferno Scepter"
                else:
                    weapon = "Savage Claws"
                monster_inventory = []
                length_weapon_list = len(player_weapon_list)
                w = random.randint(0, length_weapon_list)
                monster_inventory.append(monster_weapon_list[w])
                monster_weapon_list.remove(w)
                if monster_inventory[0] == "Standard Sword":
                    monster_weapon = "Standard Sword"
                elif monster_inventory[0] == "Poisonous Fang":
                    monster_weapon = "Poisonous Fang"
                elif monster_inventory[0] == "Inferno Claw":
                    monster_weapon = "Inferno Claw"
                elif monster_inventory[0] == "Shadow Spear":
                    monster_weapon = "Shadow Spear"
                elif monster_inventory[0] == "Thunder Whip":
                    monster_weapon = "Thunder Whip"
                elif monster_inventory[0] == "Ice Shard":
                    monster_weapon = "Ice Shard"
                return "6"
            else:
                return "Q"
        if len(player_hearts_list[0]) <= 0:
            print("You were defeated by the Cat...")
            print("""
 _____  ____   _       _____   ____   _      _____  ____ 
/  __/ /  _ \\ / \\__/| /  __/  /  _ \\ / \\ |\\ /  __/ /  __\\ 
| |  _ | / \\| | |\\/|| |  \\    | / \\| | | // |  \\   |  \\/|
| |_// | |-|| | |  || |  /_   | \\_/| | \\//  |  /_  |    /
\\____\\ \\_/ \\| \\_/  \\| \\____\\  \\____/ \\__/   \\____\\ \\_/\\_\\ 
                                                   """)
            return "1"
    else:
        return "Q"

def floor_six():
    global monster_weapon, monster_inventory, monster_die, player_die, choice, weapon, w, monster_hearts_list, player_hearts_list, player_weapon_list, player_weapon_list_dictionary, monster_weapon_list
    print_room_header("Challenge Five")
    print("----------------------------------------------------------")
    print("|                        .----.                          |")
    print("|                       ( o  o )                         |")
    print("|                       |  ^   |                         |")
    print("|                       |      |                         |")
    print("|                       '------'                         |")
    print("|                                                        |")
    print("|                ",player_hearts_list[0],"                  |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                            O                           |")
    print("|                           /|\\                          |")
    print("|                           / \\                          |")
    print("|                 ",player_hearts_list[0],"                 |")
    print("|                                                        |")
    print("|                                                        |")
    print("----------------------------------------------------------")
    print("""
        \n\nYou are in the Fourth challenge of the terrifying tower.
        There are no windows at all in the tower. And there is barely any light in the room.
        There are only a few candles scattered on the floor. Barely lighting up the room.
        But with that being said... there is an giant Potato in the middle of the room.
        Press 'F' to fight the Evil Potato
        Press 'Q' to quit the game\n""")
    while True:
        choice = input("Enter your choice\n>> ").upper()
        if choice in ["F", " F", " F ",
                      "Q", " Q", " Q "]:
            break
        else:
            print("Please enter a valid choice\n")
    if choice in ["F", " F", " F "]:
        while len(monster_hearts_list[0]) > 0 and len(player_hearts_list[0]) > 0:
            if weapon == "Shadowfang Dagger":
                player_die = random.randint(2, 5)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                stun_roll = random.randint(1, 10)
                if stun_roll % 2 == 0:
                    print(f"\nThe Shadowfang Dagger stuns the Evil Bunny with a roll of {stun_roll}!")
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Stormbringer Sword":
                player_die = random.randint(5, 10)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                paralyze_roll = random.randint(1, 4)
                if paralyze_roll == 1:
                    print(f"\nThe Stormbringer Sword strikes the Evil Bunny with a bolt of lightning and paralyzes it with a roll of {paralyze_roll}!")
                    player_die += 1
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Frostbite Axe":
                player_die = random.randint(6, 9)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                freeze_roll = random.randint(1, 2)
                if freeze_roll == 2:
                    print(f"\nThe Frostbite Axe freezes the Evil Bunny with a roll of {freeze_roll}!")
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("\n\n\n\n")
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Nightmare Scythe":
                player_die = random.randint(5, 10)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                sleep_roll = random.randint(1, 2)
                if sleep_roll % 2 == 0:
                    print(f"\nThe Nightmare Scythe puts the Evil Bunny to sleep with a roll of {sleep_roll}!")
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    time.sleep(5)
                    continue
            elif weapon == "Inferno Scepter":
                player_die = random.randint(3, 5)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                fire_roll = random.randint(1, 10)
                if fire_roll % 2 == 0:
                    print(f"\nThe Inferno Scepter strikes the Evil Potato with a rain of fire and deals an extra 1 damage with a roll of {fire_roll}!")
                    player_die += 1
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Savage Claws":
                player_die = random.randint(2, 5)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                print("----------------------------------------------------------")
                print("|                                                        |")
                print("|                                                        |")
                print("|                      ____       __                     |")
                print("|                     |    \\    /    |                   |")
                print("|                      \\  ( O O )  /                     |")
                print("|                       |    u    |                      |")
                print("|                       > - ^ ^ - <                      |")
                print("|                       > - v v - <                      |")
                print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                            O                           |")
                print("|                           /|\\                          |")
                print("|                           / \\                          |")
                print("|                 ",player_hearts_list[0],"                 |")
                print("|                                                        |")
                print("|                                                        |")
                print("----------------------------------------------------------")
                time.sleep(5)
                

                hearts_to_add = player_die
                for _ in range(hearts_to_add):
                    if len(player_hearts_list[0]) < 20:  # Assuming max health is 20 hearts
                        player_hearts_list[0] += "♥"
                    else:
                        break
            if len(monster_hearts_list[0]) > 0:
                if monster_weapon == "Standard Sword":
                    monster_die = random.randint(0, 2)
                    for _ in range(monster_die):
                        if player_hearts_list[0]:
                            player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Poisonous Fang":
                    monster_die = random.randint(2, 5)
                    poison_roll = random.randint(1, 5)
                    if poison_roll % 2 == 0:
                        monster_die += 1
                        print(f"\nThe Poisonous Fang poisons you meaning it does an extra 1 damage!")
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Inferno Claw":
                    monster_die = random.randint(3, 7)
                    inferno_roll = random.randint(1, 4)
                    if inferno_roll % 2 == 0:
                        print(f"\nThe Inferno Claw sets you on fire dealing an extra 2 damage!")
                        monster_die += 2
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Shadow Spear":
                    monster_die = random.randint(4, 6)
                    shadow_roll = random.randint(1, 2)
                    if shadow_roll == 2:
                        monster_die += 1
                        print(f"\nThe Shadow Spear deals 1 extra damage!")
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Thunder Whip":
                    monster_die = random.randint(5, 10)
                    thunder_roll = random.randint(1, 9)
                    if thunder_roll == 1:
                        monster_die += 3
                        print(f"\nThe Thunder Whip deals 3 extra damage!")
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Ice Shard":
                    monster_die = random.randint(2, 9)
                    ice_roll = random.randint(1, 10)
                    if ice_roll % 2 == 0:
                        monster_die += 1
                        print(f"\nThe Ice Shard deals 1 extra damage!")
                        monster_die += 1
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                print("\n\n\n\n")
                print("----------------------------------------------------------")
                print("|                        .----.                          |")
                print("|                       ( o  o )                         |")
                print("|                       |  ^   |                         |")
                print("|                       |      |                         |")
                print("|                       '------'                         |")
                print("|                                                        |")
                print("|                ", "".join(monster_hearts_list),"                  |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                            O                           |")
                print("|                           /|\\                          |")
                print("|                           / \\                          |")
                print("|                 ",player_hearts_list[0],"                 |")
                print("|                                                        |")
                print("|                                                        |")
                print("----------------------------------------------------------")
                time.sleep(5)
        if len(monster_hearts_list[0]) <= 0:
            print("You defeated the Cat!")
            print("----------------------------------------------------------")
            print("|                                                        |")
            print("|                                                        |")
            print("|                      _____________                     |")
            print("|                    / -----\\ /----- \\                   |")
            print("|                   |        0        |                  |")
            print("|                   |                 |                  |")
            print("|                   |                 |                  |")
            print("|                   |                 |                  |")
            print("|                    \\_______________/                   |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                                                        |")
            print("|                            O                           |")
            print("|                           /|\\                          |")
            print("|                           / \\                          |")
            print("|                 ",player_hearts_list[0],"                 |")
            print("|                                                        |")
            print("|                                                        |")
            print("----------------------------------------------------------")
            print("""
                \n\nYou have defeated the Slime! And the very second you killed the Cat \
                a chest spawned right where the Cat was. What ever will be inside??
                Press 'N' to open the chest
                Press 'Q' to quit the game\n""")
            while True:
                choice = input("Enter your choice\n>> ").upper()
                if choice in ["N", " N", " N ",
                            "Q", " Q", " Q "]:
                    break
                else:
                    print("Please enter a valid choice\n")
            if choice in ["N", " N", " N "]:
                inventory_list = []
                length_weapon_list = len(player_weapon_list)
                w = random.randint(1, length_weapon_list)
                print("\n\nThe second you open the chest you recived: ", player_weapon_list_dictionary[w], " And you automatically teleported to the fith challenge.")
                inventory_list.append(player_weapon_list[w])
                del player_weapon_list_dictionary[w]
                player_weapon_list.remove(w)
                if inventory_list[0] == "Shadowfang Dagger":
                    weapon = "Shadowfang Dagger"
                elif inventory_list[0] == "Stormbringer Sword":
                    weapon = "Stormbringer Sword"
                elif inventory_list[0] == "Frostbite Axe":
                    weapon = "Frostbite Axe"
                elif inventory_list[0] == "Nightmare Scythe":
                    weapon = "Nightmare Scythe"
                elif inventory_list[0] == "Inferno Scepter":
                    weapon = "Inferno Scepter"
                else:
                    weapon = "Savage Claws"
                monster_inventory = []
                length_weapon_list = len(player_weapon_list)
                w = random.randint(1, length_weapon_list)
                monster_inventory.append(monster_weapon_list[w])
                monster_weapon_list.remove(w)
                if monster_inventory[0] == "Standard Sword":
                    monster_weapon = "Standard Sword"
                elif monster_inventory[0] == "Poisonous Fang":
                    monster_weapon = "Poisonous Fang"
                elif monster_inventory[0] == "Inferno Claw":
                    monster_weapon = "Inferno Claw"
                elif monster_inventory[0] == "Shadow Spear":
                    monster_weapon = "Shadow Spear"
                elif monster_inventory[0] == "Thunder Whip":
                    monster_weapon = "Thunder Whip"
                elif monster_inventory[0] == "Ice Shard":
                    monster_weapon = "Ice Shard"
                return "7"
            else:
                return "Q"
        if len(player_hearts_list[0]) <= 0:
            print("You were defeated by the Cat...")
            print("""
 _____  ____   _       _____   ____   _      _____  ____ 
/  __/ /  _ \\ / \\__/| /  __/  /  _ \\ / \\ |\\ /  __/ /  __\\ 
| |  _ | / \\| | |\\/|| |  \\    | / \\| | | // |  \\   |  \\/|
| |_// | |-|| | |  || |  /_   | \\_/| | \\//  |  /_  |    /
\\____\\ \\_/ \\| \\_/  \\| \\____\\  \\____/ \\__/   \\____\\ \\_/\\_\\ 
                                                   """)
            return "1"
    else:
        return "Q"

def last_floor():
    global monster_weapon, monster_inventory, monster_die, player_die, choice, weapon, w, monster_hearts_list, player_hearts_list, player_weapon_list, player_weapon_list_dictionary, monster_weapon_list
    print_room_header("Challenge Four")
    print("----------------------------------------------------------")
    print("|                                                        |")
    print("|                      _ __/\\__ _                        |")
    print("|                    /            \\                      |")
    print("|                   |    0    0    |                     |")
    print("|                    \\      ^     /                      |")
    print("|                     /__| |_| |__\\                      |")
    print("|                                                        |")
    print("|                ",player_hearts_list[0],"                  |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                            O                           |")
    print("|                           /|\\                          |")
    print("|                           / \\                          |")
    print("|                 ",player_hearts_list[0],"                 |")
    print("|                                                        |")
    print("|                                                        |")
    print("----------------------------------------------------------")
    print("""
        \n\nYou are in the Fourth challenge of the terrifying tower.
        There are no windows at all in the tower. And there is barely any light in the room.
        There are only a few candles scattered on the floor. Barely lighting up the room.
        But with that being said... there is an giant Squid in the middle of the room.
        Press 'F' to fight the Evil Squid
        Press 'Q' to quit the game\n""")
    while True:
        choice = input("Enter your choice\n>> ").upper()
        if choice in ["F", " F", " F ",
                      "Q", " Q", " Q "]:
            break
        else:
            print("Please enter a valid choice\n")
    if choice in ["F", " F", " F "]:
        while len(monster_hearts_list[0]) > 0 and len(player_hearts_list[0]) > 0:
            if weapon == "Shadowfang Dagger":
                player_die = random.randint(2, 5)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                stun_roll = random.randint(1, 10)
                if stun_roll % 2 == 0:
                    print(f"\nThe Shadowfang Dagger stuns the Evil Bunny with a roll of {stun_roll}!")
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Stormbringer Sword":
                player_die = random.randint(5, 10)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                paralyze_roll = random.randint(1, 4)
                if paralyze_roll == 1:
                    print(f"\nThe Stormbringer Sword strikes the Evil Bunny with a bolt of lightning and paralyzes it with a roll of {paralyze_roll}!")
                    player_die += 1
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Frostbite Axe":
                player_die = random.randint(6, 9)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                freeze_roll = random.randint(1, 2)
                if freeze_roll == 2:
                    print(f"\nThe Frostbite Axe freezes the Evil Bunny with a roll of {freeze_roll}!")
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("\n\n\n\n")
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Nightmare Scythe":
                player_die = random.randint(5, 10)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                sleep_roll = random.randint(1, 2)
                if sleep_roll % 2 == 0:
                    print(f"\nThe Nightmare Scythe puts the Evil Bunny to sleep with a roll of {sleep_roll}!")
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    time.sleep(5)
                    continue
            elif weapon == "Inferno Scepter":
                player_die = random.randint(3, 5)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                fire_roll = random.randint(1, 10)
                if fire_roll % 2 == 0:
                    print(f"\nThe Inferno Scepter strikes the Evil Potato with a rain of fire and deals an extra 1 damage with a roll of {fire_roll}!")
                    player_die += 1
                    monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                    print("----------------------------------------------------------")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                      ____       __                     |")
                    print("|                     |    \\    /    |                   |")
                    print("|                      \\  ( O O )  /                     |")
                    print("|                       |    u    |                      |")
                    print("|                       > - ^ ^ - <                      |")
                    print("|                       > - v v - <                      |")
                    print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("|                            O                           |")
                    print("|                           /|\\                          |")
                    print("|                           / \\                          |")
                    print("|                 ",player_hearts_list[0],"                 |")
                    print("|                                                        |")
                    print("|                                                        |")
                    print("----------------------------------------------------------")
                    time.sleep(5)
                    continue
            elif weapon == "Savage Claws":
                player_die = random.randint(2, 5)
                print("\n" * 20)
                print(f"\nSo you decided to fight the Evil Bunny...\nYou roll a dice... and it was a {player_die}... that means you did {player_die} damage!")
                monster_hearts_list[0] = monster_hearts_list[0][:-player_die]
                print("----------------------------------------------------------")
                print("|                                                        |")
                print("|                                                        |")
                print("|                      ____       __                     |")
                print("|                     |    \\    /    |                   |")
                print("|                      \\  ( O O )  /                     |")
                print("|                       |    u    |                      |")
                print("|                       > - ^ ^ - <                      |")
                print("|                       > - v v - <                      |")
                print("|                ", "".join(monster_hearts_list) if monster_hearts_list else "","                  |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                            O                           |")
                print("|                           /|\\                          |")
                print("|                           / \\                          |")
                print("|                 ",player_hearts_list[0],"                 |")
                print("|                                                        |")
                print("|                                                        |")
                print("----------------------------------------------------------")
                time.sleep(5)
                

                hearts_to_add = player_die
                for _ in range(hearts_to_add):
                    if len(player_hearts_list[0]) < 20:  # Assuming max health is 20 hearts
                        player_hearts_list[0] += "♥"
                    else:
                        break
            if len(monster_hearts_list[0]) > 0:
                if monster_weapon == "Standard Sword":
                    monster_die = random.randint(0, 2)
                    for _ in range(monster_die):
                        if player_hearts_list[0]:
                            player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Poisonous Fang":
                    monster_die = random.randint(2, 5)
                    poison_roll = random.randint(1, 5)
                    if poison_roll % 2 == 0:
                        monster_die += 1
                        print(f"\nThe Poisonous Fang poisons you meaning it does an extra 1 damage!")
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Inferno Claw":
                    monster_die = random.randint(3, 7)
                    inferno_roll = random.randint(1, 4)
                    if inferno_roll % 2 == 0:
                        print(f"\nThe Inferno Claw sets you on fire dealing an extra 2 damage!")
                        monster_die += 2
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Shadow Spear":
                    monster_die = random.randint(4, 6)
                    shadow_roll = random.randint(1, 2)
                    if shadow_roll == 2:
                        monster_die += 1
                        print(f"\nThe Shadow Spear deals 1 extra damage!")
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Thunder Whip":
                    monster_die = random.randint(5, 10)
                    thunder_roll = random.randint(1, 9)
                    if thunder_roll == 1:
                        monster_die += 3
                        print(f"\nThe Thunder Whip deals 3 extra damage!")
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                elif monster_weapon == "Ice Shard":
                    monster_die = random.randint(2, 9)
                    ice_roll = random.randint(1, 10)
                    if ice_roll % 2 == 0:
                        monster_die += 1
                        print(f"\nThe Ice Shard deals 1 extra damage!")
                        monster_die += 1
                        for _ in range(monster_die):
                            if player_hearts_list[0]:
                                player_hearts_list[0] = player_hearts_list[0][:-1]
                print("\n\n\n\n")
                print("----------------------------------------------------------")
                print("|                                                        |")
                print("|                      _ __/\\__ _                        |")
                print("|                    /            \\                      |")
                print("|                   |    0    0    |                     |")
                print("|                    \\      ^     /                      |")
                print("|                     /__| |_| |__\\                      |")
                print("|                                                        |")
                print("|                ", "".join(monster_hearts_list),"                  |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                                                        |")
                print("|                            O                           |")
                print("|                           /|\\                          |")
                print("|                           / \\                          |")
                print("|                 ",player_hearts_list[0],"                 |")
                print("|                                                        |")
                print("|                                                        |")
                print("----------------------------------------------------------")
                time.sleep(5)
        if len(monster_hearts_list[0]) <= 0:
            print("You defeated the Squid!")
            print("""
                \n\nYou have defeated the Squid. Which was the last monster in the tower. \
                With that being said.. the second you defeated the Giant Squid you were teleported to a beautiful meadow \
                with flowers surrounding you. Each flower is a different color, colors that you have never saw before. \
                And infront of you is a plaque that says 'Thank you so much for playing my game :) I have spent 12 hours on this program ^3^ '""")
        if len(player_hearts_list[0]) <= 0:
            print("You were defeated by the Squid...")
            print("""
 _____  ____   _       _____   ____   _      _____  ____ 
/  __/ /  _ \\ / \\__/| /  __/  /  _ \\ / \\ |\\ /  __/ /  __\\ 
| |  _ | / \\| | |\\/|| |  \\    | / \\| | | // |  \\   |  \\/|
| |_// | |-|| | |  || |  /_   | \\_/| | \\//  |  /_  |    /
\\____\\ \\_/ \\| \\_/  \\| \\____\\  \\____/ \\__/   \\____\\ \\_/\\_\\ 
                                                   """)
            return "1"
    else:
        return "Q"
    
main()