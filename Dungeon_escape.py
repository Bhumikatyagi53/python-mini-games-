# GAME STORY

print("""
 ===========================================================================
                           🏰 DUNGEON ESCAPE 🏰
 ===========================================================================

GAMEPLAY     
    
You are trapped inside a dangerous dungoen.

YOUR MISSION IS TO:

✔️ Survive dangerous rooms
✔️ Collect treasure
✔️ Defeat monsters
✔️ Find the exit

Every turn you can choose a direction:

1. Left
2. Right
3. Forward     
      
Each room can contain:
      
🪙 Treasure Room  -> Gain gold
👺 Monster Room  -> Lose life or fight
💖 Healing Room  -> Gain life
💀 Trap Door     -> Lose Life
🚪 Exit Door     -> Escape the dungeon
      
RULES:
      
- You start with 3 lives
- Collect enough treasure to escape
- If lives become 0 -> GAME OVER !!

      
GOOD LUCK ADVENTURER!
=============================================================================     
""")

#CODE 

import random
import time 

lives = 3
gold = 0

rooms = ["Treasure","Monster","Healing","Trap","Exit"]

print("=" * 40)
print("🏰 WELCOME TO DUNGEON ESCAPE 🏰")
print("=" * 40)

while lives > 0:

    print("\n=================================")
    print("💖 Lives: " ,lives)
    print("🪙 Gold: ", gold)
    print("=================================")
    time.sleep(1)

    print("\nChoose a direction: ")
    print("1. Left")
    print("2. Right")
    print("3. Forward")

    choice = input("\nEnter your choice(direction):")
    print("\nYou chose direction: ",choice)
    time.sleep(1)
    print("\nMaking through the dungeon.......")

    if choice not in ["1","2","3"]:
        print("INVALID CHOICE! PLEASE ENTER 1, 2, 3")
        continue

    room = random.choice(rooms)
    print("\nYou entered a room...",room)
    time.sleep(1)

# TREASURE ROOM 

    if room == "Treasure":
       print("\n🪙 TREASURE ROOM 🪙")
       print("You found the hidden treasure!")

       gold += 10

       print("Gold +10")
       print(f"Total Gold is {gold}")

# MONSTER ROOM

    elif room == "Monster":
       print("\n👺 MONSTER ROOM 👺")
       print("A monster attacked you!")

       lives -= 1

       print("You lost 1 life")
       print(f"You have {lives} lives left.")

# HEALING ROOM

    elif room == "Healing":
       print("\n💖 HEALING ROOM 💖")
       print("You found a healing potion!")

       lives += 1

       print("Lives +1")
       print(f"You have {lives} lives now.")

# TRAP ROOM

    elif room == "Trap":
        print("\n💀 TRAP ROOM 💀")
        print("A hidden trap was activated!")

        lives -= 1
        print("You lost 1 life")
        print(f"you have {lives} lives now.")


# EXIT ROOM

    elif room == "Exit":
       print("\n🚪 EXIT ROOM 🚪")

    if gold >= 30:
        print("You collected enough gold!")
        print("🎊 YOU ESCAPED THE DUNGEON 🎊")
        break

    else:
        print("You found the exit...")
        print("But you need 50 gold to escape!")
        print("Keep exploring the dungeon.")

# GAME OVER

if lives <= 0:
    print("\n💀 GAME OVER 💀")
    print("You died inside the dungeon.")

print("\n=============================")

print("FINAL STATS")
time.sleep(1)
print("💖 Lives: ",lives)
print("🪙 Gold: ",gold)
print("\nThanks for playing")
print("\n==============================")






