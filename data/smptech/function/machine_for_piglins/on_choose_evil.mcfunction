# Reset (and disable) triggers to prevent repeated invocations
scoreboard players reset @s smptech.machine_for_piglins.player_chose_good
scoreboard players reset @s smptech.machine_for_piglins.player_chose_evil
tag @s add smptech.machine_for_piglins.evil

function smptech:machine_for_piglins/give_evil_item