# Check if each online player needs to make a choice
execute as @a[tag=smptech.machine_for_piglins.choice_pending] run function smptech:machine_for_piglins/make_choice

# Check if each online player has made a choice, and needs to be given corresponding item
execute as @a[scores={smptech.machine_for_piglins.player_chose_good=1}] run function smptech:machine_for_piglins/on_choose_good
execute as @a[scores={smptech.machine_for_piglins.player_chose_evil=1}] run function smptech:machine_for_piglins/on_choose_evil

# TODO: Sound Design

# TODO: Change this to advancement based to reduce execute as @a every tick
# Check if each online player has eaten a Jigsaw Block (Foul Sausage)
execute as @a[scores={smptech.machine_for_piglins.jigsaw_used=1..}] run function smptech:machine_for_piglins/on_consume_sausage

# Apply status effects to manpig players
execute as @a[tag=smptech.machine_for_piglins.manpig] run function smptech:apply_manpig_effects


# Check if a player has died
execute as @a[scores={smptech.machine_for_piglins.recent_death=1..}] run function smptech:machine_for_piglins/on_death