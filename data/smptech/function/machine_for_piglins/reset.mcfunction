# Initialize scoreboard for keeping track of players who need to make choice
# Scores of players who participated in the event have to be manually set to 1
scoreboard objectives remove smptech.machine_for_piglins.choice_pending
scoreboard objectives add smptech.machine_for_piglins.choice_pending dummy
scoreboard players set @a smptech.machine_for_piglins.choice_pending 0

# Initialize trigger for recording who chose what (so they won't trigger both by clicking both options)
# Does not have to be manually reset
scoreboard objectives remove smptech.machine_for_piglins.player_chose_good
scoreboard objectives add smptech.machine_for_piglins.player_chose_good trigger
scoreboard players reset @a smptech.machine_for_piglins.player_chose_good
scoreboard objectives remove smptech.machine_for_piglins.player_chose_evil
scoreboard objectives add smptech.machine_for_piglins.player_chose_evil trigger
scoreboard players reset @a smptech.machine_for_piglins.player_chose_evil

scoreboard objectives setdisplay sidebar smptech.machine_for_piglins.player_chose_good

say Reset Machine for Piglins component!