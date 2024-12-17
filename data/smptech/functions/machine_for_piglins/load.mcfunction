# Initialize trigger for recording who chose what (so they won't trigger both by clicking both options)
# Does not have to be manually reset
scoreboard objectives add smptech.machine_for_piglins.player_chose_good trigger
scoreboard objectives add smptech.machine_for_piglins.player_chose_evil trigger

# Initialize listener for tracking item uses
scoreboard objectives add smptech.machine_for_piglins.jigsaw_used minecraft.used:minecraft.jigsaw

# Initialize listener for detecting player deaths
scoreboard objectives add smptech.machine_for_piglins.recent_death deathCount

# Reset internal bookkeeping information
advancement revoke @a only smptech:machine_for_piglins/hit_pig_adjacent

say Load: M4P completed.