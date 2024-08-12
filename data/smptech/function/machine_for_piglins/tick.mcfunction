# Check if each online player needs to make a choice
execute as @a if score @s smptech.machine_for_piglins.choice_pending matches 1 run function smptech:machine_for_piglins/make_choice
execute as @a if score @s smptech.machine_for_piglins.choice_pending matches 1 run scoreboard players set @s smptech.machine_for_piglins.choice_pending 0

# Check if each online player has made a choice, and needs to be given corresponding item
execute as @a if score @s smptech.machine_for_piglins.player_chose_good matches 1 run function smptech:machine_for_piglins/on_choose_good
execute as @a if score @s smptech.machine_for_piglins.player_chose_evil matches 1 run function smptech:machine_for_piglins/on_choose_evil

# TODO: Sound Design

# Check if each online player has eaten a Jigsaw Block (Foul Sausage)
execute as @a if score @s smptech.machine_for_piglins.jigsaw_used matches 1 run function smptech:machine_for_piglins/on_consume_sausage
