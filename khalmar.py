import os
import sys
import time


# --- VISUAL TOOLKIT ---
class Colors:
    # Standard
    RED = '\033[31m'
    GREEN = '\033[32m'
    GOLD = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Bright (High Intensity)
    LAVA = '\033[91m'  # Bright Red
    LIME = '\033[92m'  # Bright Green
    SUN = '\033[93m'  # Bright Gold
    SKY = '\033[94m'  # Bright Blue
    MAGENTA = '\033[95m'  # Bright Purple
    ICE = '\033[96m'  # Bright Cyan

    # Formatting
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def slow_print(text, delay=0.005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# --- DATABASE: ITEM FLAVOR TEXT ---
ITEM_DATA = {
    "Trailworn Sigil": "An item etched by countless footsteps.",
    "Whisperleaf Charm": "A leaf that murmurs when held.",
    "Gnarled Antler Shard": "Its still warm with primal force.",
    "Fenwalker's Mark": "A mud-caked emblem of survival.",
    "Murksap Phial": "Thick, slow-moving, but faintly alive.",
    "Bogfang Relic": "It was pulled from something that did not wish to surface.",
    "Sun-Written Fragment": "Patterns are burned into ancient stone.",
    "Glassbound Dew": "Water that should not exist.",
    "Scorched Crest": "Proof that will can rival heat.",
    "Echo Pearl": "It hums with distant memories.",
    "Abyssline Scale": "It was drawn from unseen depths.",
    "Tidebound Fang": "It is salt-stained but unbroken.",
    "Obsidian Waystone": "Its worn smooth from heat and time.",
    "Cinder Reliquary": "An ash that refuses to cool.",
    "Emberheart Fragment": "Its still beating with fire.",
    "Frostbound Compass": "The needle always points forward, never back.",
    "Winterbone Talisman": "Its warm despite the frigid air.",
    "Glacier Eye Shard": "It somehow feels as if its aware you are observing it.",
    "Skycarved Relic": "It was etched by wind and effort.",
    "Ironvein Core": "Its dense with quiet strength like that of an immovable boulder.",
    "Crownstone Fragment": "It was taken from a place few reach.",
    "Equilibrium Sigil": "Its perfectly symmetrical and impossible to tilt.",
    "Grain of the Whole": "One grain, yet heavier than many.",
    "Unending Measure": "It is neither full nor empty.",
    "Memory Sigil": "Formed from moments overflowing with emotions.",
    "Aetherbound Anchor": "It refuses to drift away, remaining bastioned.",
    "True Name Shard": "It is much heavier than it looks..."
}


# --- UI SYSTEMS ---
def show_quest_log(wis, wll, pat, det, inv):
    clear_screen()
    print(f"{Colors.GOLD}╔══════════════════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.GOLD}║                ESSENCE & POSSESSIONS                 ║{Colors.END}")
    print(f"{Colors.GOLD}╠══════════════════════════════════════════════════════╣{Colors.END}")
    print(f"  Wisdom:   {wis:<5} Will:     {wll:<5}")
    print(f"  Patience: {pat:<5} Detachment: {det:<5}")
    print(f"{Colors.GOLD}╠══════════════════════════════════════════════════════╣{Colors.END}")
    print(f"  INVENTORY:")
    if not inv:
        print("    (Empty)")
    for item in inv:
        desc = ITEM_DATA.get(item, "A mysterious artifact.")
        print(f"  • {Colors.BOLD}{item}{Colors.END}: {desc}")
    print(f"{Colors.GOLD}╚══════════════════════════════════════════════════════╝{Colors.END}")
    input("\n[Press Enter to return to your journey]")


def get_choice(options, wis, wll, pat, det, inv, art="", art_color=""):
    while True:
        print("\n" + "─" * 45)
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")

        choice_raw = input(f"\n{Colors.BOLD}Choice (1-{len(options)}) or [0] Essence Log: {Colors.END}")

        if choice_raw == '0':
            show_quest_log(wis, wll, pat, det, inv)
            clear_screen()
            if art: print(art_color + art + Colors.END)
            print(f"{Colors.BOLD}Returning to the path...{Colors.END}")
            continue

        try:
            choice = int(choice_raw)
            if 1 <= choice <= len(options):
                return choice
            print("That choice does not exist in this realm.")
        except ValueError:
            print("The world does not understand that command.")


# --- UPDATED ART ASSETS ---
TITLE_ART = f"""
{Colors.SUN}   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
   █░░░░░░░░░░░░░   {Colors.ICE}AN' KHALMAR{Colors.SUN}   ░░░░░░░░░░░░░░░░░░░█
   █░░░░░░░░░░░░ {Colors.RED}A FRACTURED WORLD{Colors.SUN} ░░░░░░░░░░░░░░░░░░█
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{Colors.END}
"""

FOREST_ART = r"""
          ▓▓▓▓      ▒▒▒▒      ▓▓▓▓
         ▓▓▓▓▓▓    ▒▒▒▒▒▒    ▓▓▓▓▓▓
          ████      ████      ████
           ██        ██        ██
    ───────██────────██────────██────────
"""

MARSH_ART = r"""
      ░░  ░░      ░░  ░░      ░░  ░░
     ▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒
    ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

DESERT_ART = r"""
             ▲              ▲
            ▓▓▓            ▓▓▓
           ▓▓▓▓▓    ▲     ▓▓▓▓▓
    ______▓▓▓▓▓▓▓__▓▓▓___▓▓▓▓▓▓▓______
"""

OCEAN_ART = r"""
       _      _      _      _      _
     _/ \_  _/ \_  _/ \_  _/ \_  _/ \_
    <     ><     ><     ><     ><     >
     \___/  \___/  \___/  \___/  \___/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

VOLCANO_ART = r"""
              (  ░░  )
             (  ▒▒▒▒  )
            /   ▓▓▓▓   \
           /    ████    \
          /   /▓▓▓▓▓▓\   \
    _____/___/████████\___\_____
"""

TUNDRA_ART = r"""
       * ❄️    * ❄️    * ❄️
      /▒\  /▒\  /▒\  /▒\  /▒\  /▒\
     /▒▒▒\/▒▒▒\/▒▒▒\/▒▒▒\/▒▒▒\/▒▒▒\
    [_______________________________]
"""

MOUNTAIN_ART = r"""
               ▲
              ███      ▲
         ▲   █████    ███
        ███ ███████  █████
    ___█████████████████████___
"""

SCALES_ART = r"""
           ▒▒▒▒▒  █  ▒▒▒▒▒
            ▒▒▒   █   ▒▒▒
             ▒    █    ▒
            █████████████
                  █
"""

WELKIN_ART = r"""
        ☁️   ☁️          ☁️   ☁️
      ░░░░░░░░        ░░░░░░░░
     ▒▒▒▒▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒▒▒
    ░░░░░░░░░░░░    ░░░░░░░░░░░░
"""

# --- GAME START ---
clear_screen()
print(TITLE_ART)
slow_print("Welcome to An' Khalmar! A fractured world where your choices reflect your very essence.")
if input("\nBegin your adventure? (Y/N): ").upper() != 'Y':
    print("You are not ready yet. Life does not wait...")
    sys.exit()

wisdom, patience, will, detachment = 0, 0, 0, 0
inventory = []

# --- 1. FOREST ---
clear_screen()
print(Colors.GREEN + FOREST_ART + Colors.END)
slow_print(
    "Your journey begins in the ancient forest. You step beneath a canopy of ancient trees. Sunlight filters through leaves that whisper in a language older than memory. Paths twist and fade into moss and shadow. Every direction feels intentional.")
opts = ["Follow the Paths", "Listen to the Woods", "Hunt the Presence", "Leave"]
choice = get_choice(opts, wisdom, will, patience, detachment, inventory, FOREST_ART, Colors.GREEN)

if choice == 1:
    item = "Trailworn Sigil";
    wisdom += 1;
    inventory.append(item)
    slow_print(f"\nYou received a {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
elif choice == 2:
    item = "Whisperleaf Charm";
    patience += 1;
    inventory.append(item)
    slow_print(f"\nYou received a {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
elif choice == 3:
    item = "Gnarled Antler Shard";
    will += 1;
    inventory.append(item)
    slow_print(f"\nYou received a {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
else:
    slow_print("\nYou turn away. The air grows heavier. Roots give way to mud, and birdsong fades.")
    detachment += 1
input("\n[Enter to move on]")

# --- 2. MARSH ---
clear_screen()
print(Colors.PURPLE + MARSH_ART + Colors.END)
slow_print(
    "The ground softens as the forest gives way to mist and stagnant water. Bubbles rise slowly from dark pools. Each step threatens to pull you deeper than you intend. The bog remembers travelers.")
opts = ["Trace the Dry Ground", "Harvest the Mire", "Stir What Sleeps Below", "Leave"]
choice = get_choice(opts, wisdom, will, patience, detachment, inventory, MARSH_ART, Colors.PURPLE)

if choice == 1:
    item = "Fenwalker's Mark";
    wisdom += 1;
    inventory.append(item)
    slow_print(f"\nYou received {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
elif choice == 2:
    item = "Murksap Phial";
    patience += 1;
    inventory.append(item)
    slow_print(f"\nYou received a {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
elif choice == 3:
    item = "Bogfang Relic";
    will += 1;
    inventory.append(item)
    slow_print(f"\nYou received a {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
else:
    slow_print("\nYou pull free from the mire. Mist thins, water dries, and the land begins to crack.")
    detachment += 1
input("\n[Enter to move on]")

# --- 3. DESERT ---
clear_screen()
print(Colors.GOLD + DESERT_ART + Colors.END)
slow_print(
    "Heat crashes down like a physical force. Endless dunes stretch to the horizon. Ruins half-buried hint at civilizations that lost. The desert offers clarity or madness.")
opts = ["Read the Dunes", "Collect the Mirage", "Challenge the Sun", "Leave"]
choice = get_choice(opts, wisdom, will, patience, detachment, inventory, DESERT_ART, Colors.GOLD)

if choice == 1:
    item = "Sun-Written Fragment";
    wisdom += 1;
    inventory.append(item)
    slow_print(f"\nYou received a {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
elif choice == 2:
    item = "Glassbound Dew";
    patience += 1;
    inventory.append(item)
    slow_print(f"\nYou received {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
elif choice == 3:
    item = "Scorched Crest";
    will += 1;
    inventory.append(item)
    slow_print(f"\nYou received a {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
else:
    slow_print("\nYou leave. The horizon stretches wide as sand cools.")
    detachment += 1
input("\n[Enter to move on]")

# --- 4. OCEAN ---
clear_screen()
print(Colors.BLUE + OCEAN_ART + Colors.END)
slow_print(
    "The land ends abruptly, swallowed by an endless sea. Waves roll in with a rhythm that feels deliberate. Beneath the surface, shadows move. The water promises wonder and oblivion.")
opts = ["Dive Below", "Cast into the Deep", "Challenge the Depths", "Leave"]
choice = get_choice(opts, wisdom, will, patience, detachment, inventory, OCEAN_ART, Colors.BLUE)

if choice == 1:
    item = "Echo Pearl";
    wisdom += 1;
    inventory.append(item)
    slow_print(f"\nYou received an {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
elif choice == 2:
    item = "Abyssline Scale";
    patience += 1;
    inventory.append(item)
    slow_print(f"\nYou received a {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
elif choice == 3:
    item = "Tidebound Fang";
    will += 1;
    inventory.append(item)
    slow_print(f"\nYou received a {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
else:
    slow_print("\nYou turn from the sea. The air thickens with the scent of sulfur.")
    detachment += 1
input("\n[Enter to move on]")

# --- 5. VOLCANO ---
clear_screen()
print(Colors.RED + VOLCANO_ART + Colors.END)
slow_print(
    "The air grows heavy with ash. Cracks in the earth pulse like a heartbeat. The ground trembles constantly. Creation and destruction are the same act here.")
opts = ["Descend the Slopes", "Gather the Ash", "Face the Flames", "Leave"]
choice = get_choice(opts, wisdom, will, patience, detachment, inventory, VOLCANO_ART, Colors.RED)

if choice == 1:
    item = "Obsidian Waystone";
    wisdom += 1;
    inventory.append(item)
    slow_print(f"\nYou received a {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
elif choice == 2:
    item = "Cinder Reliquary";
    patience += 1;
    inventory.append(item)
    slow_print(f"\nYou received a {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
elif choice == 3:
    item = "Emberheart Fragment";
    will += 1;
    inventory.append(item)
    slow_print(f"\nYou received an {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
else:
    slow_print("\nYou retreat. Heat drains away. Ash becomes snow. Fire no longer answers.")
    detachment += 1
input("\n[Enter to move on]")

# --- 6. TUNDRA ---
clear_screen()
print(Colors.WHITE + TUNDRA_ART + Colors.END)
slow_print(
    "The world falls silent. Snow stretches in every direction. Your breath fogs the air. Something ancient watches from the cold.")
opts = ["Chart the White Expanse", "Endure the Cold", "Provoke the Silent Watcher", "Leave"]
choice = get_choice(opts, wisdom, will, patience, detachment, inventory, TUNDRA_ART, Colors.WHITE)

if choice == 1:
    item = "Frostbound Compass";
    wisdom += 1;
    inventory.append(item)
    slow_print(f"\nYou received a {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
elif choice == 2:
    item = "Winterbone Talisman";
    patience += 1;
    inventory.append(item)
    slow_print(f"\nYou received a {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
elif choice == 3:
    item = "Glacier Eye Shard";
    will += 1;
    inventory.append(item)
    slow_print(f"\nYou received a {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
else:
    slow_print("\nYou press onward. The flat white expanse begins to rise.")
    detachment += 1
input("\n[Enter to move on]")

# --- 7. MOUNTAINS ---
clear_screen()
print(Colors.CYAN + MOUNTAIN_ART + Colors.END)
slow_print(
    "Jagged peaks rise above you. The air is thin and sharp. Every sound echoes farther than it should. Only those who endure reach the summit.")
opts = ["Climb the Ancient Paths", "Mine the Heights", "Defy the Summit", "Leave"]
choice = get_choice(opts, wisdom, will, patience, detachment, inventory, MOUNTAIN_ART, Colors.CYAN)

if choice == 1:
    item = "Skycarved Relic";
    wisdom += 1;
    inventory.append(item)
    slow_print(f"\nYou received {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
elif choice == 2:
    item = "Ironvein Core";
    patience += 1;
    inventory.append(item)
    slow_print(f"\nYou received an {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
elif choice == 3:
    item = "Crownstone Fragment";
    will += 1;
    inventory.append(item)
    slow_print(f"\nYou have received a {Colors.BOLD}'{item}'{Colors.END}.\n{ITEM_DATA[item]}", 0.015)
else:
    slow_print("\nYou have decided to leave. Stone crumbles in surrender.")
    detachment += 1
input("\n[Enter to face judgment]")

# --- HIDDEN PATH CHECK ---
if max(wisdom, will, patience) - min(wisdom, will, patience) <= 1:
    clear_screen()
    print(Colors.GOLD + SCALES_ART + Colors.END)
    slow_print("Stone gives way to drifting sand. Every step feels weightless. You stand before the Scales of Sands.")
    opts = ["Step onto the Scales", "Still the Flowing Sand", "Witness the Measure", "Leave"]
    choice = get_choice(opts, wisdom, will, patience, detachment, inventory, SCALES_ART, Colors.GOLD)
    if choice == 1:
        item = "Equilibrium Sigil";
        inventory.append(item);
        slow_print(f"Received: {item}. {ITEM_DATA[item]}")
    elif choice == 2:
        item = "Grain of the Whole";
        inventory.append(item);
        slow_print(f"Received: {item}. {ITEM_DATA[item]}")
    elif choice == 3:
        item = "Unending Measure";
        inventory.append(item);
        slow_print(f"Received: {item}. {ITEM_DATA[item]}")
    else:
        slow_print("The sand stills. The scales vanish. The sky opens within you.")
    input("\n[Enter to ascend]")
else:
    clear_screen()
    slow_print("The mountain simply ends. You rise. The sky does not open. It absorbs you.")
    input("\n[Enter to ascend]")

# --- 8. WELKIN ---
clear_screen()
print(Colors.PURPLE + WELKIN_ART + Colors.END)
slow_print("You stand suspended between sky and thought. Clouds drift like forgotten dreams. This realm reveals truth.")
opts = ["Follow the Echoes", "Hold Your Ground", "Confront Yourself", "Leave"]
choice = get_choice(opts, wisdom, will, patience, detachment, inventory, WELKIN_ART, Colors.PURPLE)

if choice == 1:
    item = "Memory Sigil";
    inventory.append(item);
    slow_print(f"Received: {item}. {ITEM_DATA[item]}")
elif choice == 2:
    item = "Aetherbound Anchor";
    inventory.append(item);
    slow_print(f"Received: {item}. {ITEM_DATA[item]}")
elif choice == 3:
    item = "True Name Shard";
    inventory.append(item);
    slow_print(f"Received: {item}. {ITEM_DATA[item]}")
else:
    slow_print("The journey ends.")

# --- FINAL CHRONICLE ---
clear_screen()
slow_print(f"{Colors.BOLD}--- THE FINAL CHRONICLE ---{Colors.END}")
time.sleep(1)

stats = [wisdom, will, patience]
if detachment >= 5:
    title = f"{Colors.PURPLE}The Silent Walker{Colors.END}"
    truth = "You walk in shadows and light with no emotion, simply observing."
elif max(stats) - min(stats) <= 1 and sum(stats) > 0:
    title = f"{Colors.GOLD}The Bearer of Scales{Colors.END}"
    truth = "You are the Arbiter of Oneself and have reached self-mastery."
elif wisdom >= max(will, patience):
    title = f"{Colors.CYAN}The Listener Beyond Horizons{Colors.END}"
    truth = "You have knowledge and insight surpassing that of what is visible."
elif will >= max(wisdom, patience):
    title = f"{Colors.RED}The Defiant Ascendant{Colors.END}"
    truth = "You burn your own path no matter who or what stands in your way."
else:
    title = f"{Colors.GREEN}The Keeper who Remains{Colors.END}"
    truth = "You are time-tested and stable like the world tree Yggdrasil."

print(f"\nTitle: {title}")
print(f"Truth: {truth}")
print(f"Final Inventory: {', '.join(inventory) if inventory else 'Empty'}")
print(f"\n{Colors.BOLD}Thank you for playing An' Khalmar.{Colors.END}")
# Catch-all
else:
    print("You have completed your journey. You have earned the title of 'The Challenger'. May you rise again to the challenges you will face...")
