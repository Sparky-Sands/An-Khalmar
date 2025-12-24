#this is my first game I am creating so hold onto your seats ladies and gentlemen


#welcome
print("Welcome to An' Khalmar! A fractured world where your choices reflect your very essence.")
start = input("Would you like to begin your adventure? (Y/N)")

if start == 'Y':
    print("Let the tale of your adventure begin.")
else:
    print("You are not ready yet. That is ok, but remember life does not wait until you are ready...")

#hidden values
wisdom = 0
patience = 0
will = 0
detachment = 0


#hidden path balance
def hidden_path_unlocked(wisdom, will, patience):
    return max(wisdom, will, patience) - min(wisdom, will, patience) <= 1



print(
'Your journey begins in the ancient forest. You step beneath a canopy of ancient trees. Sunlight filters through leaves that whisper in a language older than memory. The air is alive with unseen movement, and the forest seems to watch you as much as you watch it. Paths twist and fade into moss and shadow. Every direction feels intentional. You have arrived in the Forest. '
)
print('The land seems to wait for your decision.')
#forest
forest_outcome = int(input("What do you do?\n 1.Follow the Paths\n 2.Listen to the Woods\n 3.Hunt the Presence\n 4.Leave\n"))
if forest_outcome == 1:
    print("You received a 'Trailworn Sigil'.\nAn item etched by countless footsteps. ")
    wisdom += 1
elif forest_outcome == 2:
    print("You received a 'Whisperleaf Charm'.\nA leaf that murmurs when held")
    patience += 1
elif forest_outcome == 3:
    print("You received a 'Gnarled Antler Shard'.\nIts still warm with primal force.")
    will += 1
elif forest_outcome == 4:
    print('You turn away from the whispering trees. The forest does not stop you, but the air grows heavier with every step. Roots give way to mud, and birdsong fades into distant croaks and silence. The ground ahead no longer forgives mistakes.')
    detachment += 1
else:
    print('Adventures allow for freedom of choice, but this is not one of those choices...')


#marsh/bog
print('The ground softens beneath your feet as the forest gives way to mist and stagnant water. Reeds sway though there is no wind. Bubbles rise slowly from dark pools, breaking the silence. Each step threatens to pull you deeper than you intend. The bog does not welcome travelers but it remembers them. You have arrived in the Marsh.')
marsh_outcome = int(input('What do you do?\n 1.Trace the Dry Ground\n 2.Harvest the Mire\n 3.Stir What Sleeps Below\n 4.Leave\n'))
if marsh_outcome == 1:
    print("You received 'Fenwalker's Mark'.\nA mud-caked emblem of survival.")
    wisdom += 1
elif marsh_outcome == 2:
    print("You received a 'Murksap Phial'.\nThick, slow-moving, but faintly alive.")
    patience += 1
elif marsh_outcome == 3:
    print("You received a 'Bogfang Relic'.\nIt was pulled from something that did not wish to surface.")
    will += 1
elif marsh_outcome == 4:
    print("You pull free from the mire. Mist thins, water dries, and the land begins to crack. The world no longer hides its dangers.")
    detachment += 1
else:
    print('Adventures allow for freedom of choice, but this is not one of those choices...')

#desert
print('Heat crashes down upon you like a physical force. Endless dunes stretch to the horizon, their shapes shifting with every passing moment. Ruins half-buried by sand hint at civilizations that challenged the sun — and lost. The desert offers clarity or madness, depending on your resolve. You have arrived in the Desert.')
desert_outcome = int(input('What do you do?\n 1.Read the Dunes\n 2.Collect the Mirage\n 3.Challenge the Sun\n 4.Leave\n'))
if desert_outcome == 1:
    print("You received a 'Sun-Written Fragment'.\nPatterns are burned into ancient stone.")
    wisdom += 1
elif desert_outcome == 2:
    print("You received 'Glassbound Dew'.\nWater that should not exist.")
    patience += 1
elif desert_outcome == 3:
    print("You received a 'Scorched Crest'.\nProof that will can rival heat.")
    will += 1
elif desert_outcome == 4:
    print('You leave the dunes behind. The horizon stretches wide as sand cools beneath your feet. What was barren is now unfathomable.')
    detachment += 1
else:
    print('Adventures allow for freedom of choice, but this is not one of those choices...')

#ocean
print('The land ends abruptly, swallowed by an endless sea. Waves roll in with a rhythm that feels deliberate, as though the ocean breathes. Beneath the surface, shadows move where light cannot reach. The water promises both wonder and oblivion. You have arrived at the Ocean.')
ocean_outcome = int(input('What do you do?\n 1.Dive Below\n 2.Cast into the Deep\n 3.Challenge the Depths\n 4.Leave\n'))
if ocean_outcome == 1:
    print("You received an 'Echo Pearl'.\nIt hums with distant memories.")
    wisdom += 1
elif ocean_outcome == 2:
    print("You received  a 'Abyssline Scale'.\nIt was drawn from unseen depths.")
    patience += 1
elif ocean_outcome == 3:
    print("You received a 'Tidebound Fang'.\nIt is salt-stained but unbroken.")
    will += 1
elif ocean_outcome == 4:
    print('You turn from the sea. Waves fall silent behind you as the air thickens and the scent of sulfur replaces salt. The land rises and darkens, glowing faintly from within. The calm gives way to fury.')
    detachment += 1
else:
    print('Adventures allow for freedom of choice, but this is not one of those choices...')

#volcano
print('The air grows heavy with ash and heat. Cracks in the earth glow faintly, pulsing like a heartbeat. The ground trembles, not violently but constantly,as if the land itself is barely restrained. This is a place where creation and destruction are the same act. You have arrived at the Volcano.')
volcano_outcome = int(input('What do you do?\n 1.Descend the Slopes\n 2.Gather the Ash\n 3.Face the Flames\n 4.Leave\n'))
if volcano_outcome == 1:
    print("You received a 'Obsidian Waystone'.\nIts worn smooth from heat and time.")
    wisdom += 1
elif volcano_outcome == 2:
    print("You received a 'Cinder Reliquary'.\nAn ash that refuses to cool.")
    patience += 1
elif volcano_outcome == 3:
    print("You received an 'Emberheart Fragment'.\nIts still beating with fire.")
    will += 1
elif volcano_outcome == 4:
    print('You retreat from the flames. Heat drains from the air with unnatural speed. Ash becomes snow, and the ground hardens beneath your steps. The world grows quiet. Too quiet. Fire no longer answers you.')
    detachment += 1
else:
    print('Adventures allow for freedom of choice, but this is not one of those choices...')

#tundra
print('The world falls silent. Snow stretches in every direction, unbroken and unforgiving. Your breath fogs the air, each exhale a reminder that survival here is never guaranteed. In the distance, something ancient watches from the cold. You have arrived in the Tundra.')
tundra_outcome = int(input('What do you do?\n 1.Chart the White Expanse\n 2.Endure the Cold\n 3.Provoke the Silent Watcher\n 4.Leave\n'))
if tundra_outcome == 1:
    print("You received a 'Frostbound Compass'.\nThe needle always points forward, never back.")
    wisdom += 1
elif tundra_outcome == 2:
    print("You received a 'Winterbone Talisman'.\nIts warm despite the frigid air.")
    patience += 1
elif tundra_outcome == 3:
    print("You received a 'Glacier Eye Shard'.\nIt somehow feels as if its aware you are observing it.")
    will += 1
elif tundra_outcome == 4:
    print('You press onward through the cold. The flat white expanse begins to rise, snow clinging to jagged stone. The path ahead must be earned.')
    detachment += 1
else:
    print('Adventures allow for freedom of choice, but this is not one of those choices.')

#mountainous region
print('Jagged peaks rise above you, piercing the sky. The climb ahead is steep, the air thin and sharp. Every sound echoes, carrying farther than it should. From this height, the world feels smaller and more fragile. Only those who endure reach the summit. You have arrived in the Mountains.')
mountain_outcome = int(input('What do you do?\n 1.Climb the Ancient Paths\n 2.Mine the Heights\n 3.Defy the Summit\n 4.Leave\n'))
if mountain_outcome == 1:
    print("You received 'Skycarved Relic'.\nIt was etched by wind and effort.")
    wisdom += 1
elif mountain_outcome == 2:
    print("You received an 'Ironvein Core'.\nIts dense with quiet strength like that of an immovable boulder.")
    patience += 1
elif mountain_outcome == 3:
    print("You have received a 'Crownstone Fragment'.\nIt was taken from a place few reach")
    will += 1
elif mountain_outcome == 4:
    print('You have decided to leave.')
    detachment += 1
else:
    print('Adventures allow for freedom of choice, but this is not one of those choices.')

#determine whether hidden path is unlocked
if hidden_path_unlocked(wisdom, will, patience):
    # scales of sands
    print('You leave the summit behind. Stone gives way to drifting sand suspended in the air. Every step feels measured, yet weightless.')
    sands_outcome = int(input('What do you do?\n 1.Step onto the Scales\n 2.Still the Flowing Sand\n 3.Witness the Measure\n 4.Leave\n'))
    if sands_outcome == 1:
        print("You received an 'Equilibrium Sigil'.\nIts perfectly symmetrical and impossible to tilt no matter how hard you try.")
    elif sands_outcome == 2:
        print("You received 'Grain of the Whole'.\nOne grain, yet heavier than many. A true homage to the parts are greater than the whole.")
    elif sands_outcome == 3:
        print("You received the 'Unending Measure'.\nIt is neither full nor empty. A representation of human potential possibly?")
    elif sands_outcome == 4:
        print('The sand stills. The scales vanish.\nFor the first time, nothing is weighed. The sky opens not above you, but within you.')
    else:
        print('Adventures allow for freedom of choice, but this is not one of those choices.')
else:
    print('You leave the summit behind. The wind howls louder than before, stripping sound from the world. Stone crumbles beneath your final steps, not in collapse but in surrender. There is no threshold. No scale. No moment of judgment. The mountain simply ends. You rise. Not because you are ready, but because nothing remains to resist you. The sky does not open. It absorbs you.')

#welkin
print('The ground fades beneath your feet. You stand suspended between sky and thought, where clouds drift like forgotten dreams. The air hums softly, resonating with every choice you have made to reach this place. This realm does not test strength, it reveals truth. You have arrived in the Welkin.')
welkin_outcome = int(input('What do you do?\n 1.Follow the Echoes\n 2.Hold Your Ground\n 3.Confront Yourself\n 4.Leave\n'))
if welkin_outcome == 1:
    print("You received a 'Memory Sigil'.\nIt was formed from momements overflowing with emotions.")
elif welkin_outcome == 2:
    print("You received an 'Aetherbound Anchor'.\nNo matter how its placed it refuses to drift away remaining bastioned where placed.")
elif welkin_outcome == 3:
    print("You received the 'True Name Shard'.\nIt is much heavier that it looks...")
elif welkin_outcome == 4:
    print('You have finished the journey.')

# Outcomes
# Rebuild stats dynamically
stats_list = [wisdom, will, patience]
total_stats = sum(stats_list)

# Threshold for extreme detachment
EXTREME_DETACHMENT = 5  # number of times the player leaves to trigger Silent Walker

# Check for extreme detachment first
if detachment >= EXTREME_DETACHMENT:
    print("You have earned the title of 'The Silent Walker'. You walk in shadows and light with no emotion, simply observing the world as if you are not part of it.")

# Check for balance (Bearer of Scales)
elif max(stats_list) - min(stats_list) <= 1 and total_stats > 0:
    print("You have earned the title of 'The Bearer of Scales'. You are the Arbiter of Oneself and have reached self-mastery.")

# Otherwise, give title based on highest stat
elif wisdom >= will and wisdom >= patience:
    print("You have earned the title of 'The Listener Beyond Horizons'. You have knowledge and insight surpassing that of what is visible.")
elif will >= wisdom and will >= patience:
    print("You have earned the title of 'The Defiant Ascendant'. You burn your own path no matter who or what stands in your way.")
elif patience >= wisdom and patience >= will:
    print("You have earned the title of 'The Keeper who Remains'. You are time-tested and stable like the world tree Yggdrasil.")

# Catch-all
else:
    print("You have completed your journey. You have earned the title of 'The Challenger'. May you rise again to the challenges you will face...")
