scoreboard players add minutes uhc_timer 1

# Scheduled events
execute if score minutes uhc_timer matches 15 run function uhc:border/start_shrink
scoreboard players operation #min_remaining uhc_timer = #minutes_end uhc_timer
scoreboard players operation #min_remaining uhc_timer -= minutes uhc_timer
execute if score #min_remaining uhc_timer matches 30 run title @a title {"text":"30 minutes remaining!","color":"yellow"}
execute if score #min_remaining uhc_timer matches 15 run function uhc:deathmatch

execute unless score minutes uhc_timer >= #minutes_end uhc_timer run schedule function uhc:time/min 60s