
import random

# INTERACTIVE ADVENTURE GAME

player_name = input("Enter your adventurer name: ")

health = 100
attack = 20
inventory = ["Small Potion"]
achievements = []
current_location = "Village"
game_running = True
has_treasure = False

locations = {
    "Village": ["Forest", "Cave"],
    "Forest": ["Village", "Castle"],
    "Cave": ["Village", "Castle"],
    "Castle": ["Forest", "Cave"]
}

enemies = {
    "Forest": {"name": "Wolf", "health": 35, "attack": 12},
    "Cave": {"name": "Goblin", "health": 45, "attack": 15},
    "Castle": {"name": "Dark Knight", "health": 60, "attack": 18}
}

print("\nWelcome,", player_name + "!")
print("Your mission is to find the legendary treasure hidden in the Castle.")
print("Explore locations, collect items, defeat enemies, and survive!")

while game_running:

    print("\n" + "=" * 40)
    print("PLAYER:", player_name)
    print("HEALTH:", health)
    print("ATTACK POWER:", attack)
    print("LOCATION:", current_location)
    print("INVENTORY:", inventory)
    print("=" * 40)

    print("\n1. Explore a new location")
    print("2. View inventory")
    print("3. Use a potion")
    print("4. View achievements")
    print("5. Quit game")

    choice = input("\nChoose an action: ")

    if choice == "1":

        available_locations = locations[current_location]

        print("\nAvailable locations:")

        for i in range(len(available_locations)):
            print(i + 1, ".", available_locations[i])

        try:
            destination = int(input("Choose a location number: "))

            if destination < 1 or destination > len(available_locations):
                print("Invalid location number.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        current_location = available_locations[destination - 1]

        print("\nYou travelled to", current_location + "!")

        if current_location not in achievements:
            achievements.append(current_location + " Explorer")

        if current_location == "Village":
            print("You are safe in the village.")
            continue

        if current_location == "Forest" and "Magic Sword" not in inventory:
            print("\nYou discovered a Magic Sword!")
            inventory.append("Magic Sword")
            attack = attack + 10

            if "Sword Collector" not in achievements:
                achievements.append("Sword Collector")

        if current_location in enemies:

            enemy = enemies[current_location]

            enemy_health = enemy["health"]
            enemy_attack = enemy["attack"]

            print("\nA", enemy["name"], "appeared!")

            while enemy_health > 0 and health > 0:

                print("\nYour Health:", health)
                print(enemy["name"] + "'s Health:", enemy_health)

                print("\n1. Attack")
                print("2. Run away")

                battle_choice = input("Choose your action: ")

                if battle_choice == "1":

                    damage = random.randint(attack - 5, attack + 5)
                    enemy_health = enemy_health - damage

                    print("\nYou dealt", damage, "damage!")

                    if enemy_health <= 0:
                        print("\nYou defeated the", enemy["name"] + "!")

                        if "Enemy Slayer" not in achievements:
                            achievements.append("Enemy Slayer")

                        if current_location == "Castle":
                            has_treasure = True
                            print("\nYou discovered the legendary treasure!")

                            if "Treasure Hunter" not in achievements:
                                achievements.append("Treasure Hunter")

                        else:
                            if "Health Potion" not in inventory:
                                inventory.append("Health Potion")
                                print("You found a Health Potion!")

                        break

                    enemy_damage = random.randint(enemy_attack - 3, enemy_attack + 3)
                    health = health - enemy_damage

                    print("The enemy attacked you for", enemy_damage, "damage!")

                elif battle_choice == "2":
                    print("You escaped from the battle!")
                    break

                else:
                    print("Invalid choice. Try again.")

            if health <= 0:
                print("\nYou have been defeated!")
                print("GAME OVER!")
                game_running = False

    elif choice == "2":

        print("\nYour Inventory:")

        if len(inventory) == 0:
            print("Your inventory is empty.")

        else:
            for item in inventory:
                print("-", item)

    elif choice == "3":

        if "Small Potion" in inventory:
            health = health + 30

            if health > 100:
                health = 100

            inventory.remove("Small Potion")

            print("\nYou used a Small Potion.")
            print("Your health is now:", health)

        elif "Health Potion" in inventory:
            health = health + 50

            if health > 100:
                health = 100

            inventory.remove("Health Potion")

            print("\nYou used a Health Potion.")
            print("Your health is now:", health)

        else:
            print("\nYou don't have any potions!")

    elif choice == "4":

        print("\nYour Achievements:")

        if len(achievements) == 0:
            print("No achievements unlocked yet.")

        else:
            for achievement in achievements:
                print("-", achievement)

    elif choice == "5":

        print("\nThanks for playing,", player_name + "!")
        game_running = False

    else:
        print("\nInvalid choice. Please select between 1 and 5.")

    if has_treasure and game_running:
        print("\nCongratulations,", player_name + "!")
        print("You completed the adventure and found the legendary treasure!")
        print("YOU WIN!")
        game_running = False
