# Initialize trigger for recording who chose what (so they won't trigger both by clicking both options)
# Does not have to be manually reset
scoreboard objectives remove smptech.machine_for_piglins.player_chose_good
scoreboard objectives add smptech.machine_for_piglins.player_chose_good trigger
scoreboard players reset @a smptech.machine_for_piglins.player_chose_good
scoreboard objectives remove smptech.machine_for_piglins.player_chose_evil
scoreboard objectives add smptech.machine_for_piglins.player_chose_evil trigger
scoreboard players reset @a smptech.machine_for_piglins.player_chose_evil

# Initialize listener for tracking item uses
scoreboard objectives remove smptech.machine_for_piglins.jigsaw_used
scoreboard objectives add smptech.machine_for_piglins.jigsaw_used minecraft.used:minecraft.jigsaw
scoreboard players set @a smptech.machine_for_piglins.jigsaw_used 0

# Initialize listener for detecting player deaths
scoreboard objectives remove smptech.machine_for_piglins.recent_death
scoreboard objectives add smptech.machine_for_piglins.recent_death deathCount
scoreboard players set @a smptech.machine_for_piglins.recent_death 0

scoreboard objectives setdisplay sidebar smptech.machine_for_piglins.recent_death

say Reset Machine for Piglins component!