scoreboard players add minutes uhc_timer 1

scoreboard players operation #min_remaining uhc_timer = #minutes_end uhc_timer
scoreboard players operation #min_remaining uhc_timer -= minutes uhc_timer

# Scheduled events
execute if score minutes uhc_timer matches 10 run tellraw @a [{"text":"5 minutes","color":"yellow"},{"text":" till ","color":"gray"},{"text":"border shrinking","italic":true,"color":"gray"},{"text":" and ","italic":false,"color":"gray"},{"text":"PVP","italic":true,"color":"gray"},{"text":" are enabled!","italic":false,"color":"gray"}]

execute if score minutes uhc_timer matches 15 run function uhc:border/start_shrink
execute if score minutes uhc_timer matches 15 run team empty uhc_grace_period
execute if score minutes uhc_timer matches 15 run title @a subtitle {"text":"Grace period has also ended.","color":"white"}
execute if score minutes uhc_timer matches 15 run tellraw @a {"text":"Grace period has ended.","color":"yellow"}

execute if score #min_remaining uhc_timer matches 30 run title @a title {"text":"30 minutes remaining!","color":"yellow"}

execute if score #min_remaining uhc_timer matches 15 run function uhc:deathmatch

execute unless score minutes uhc_timer >= #minutes_end uhc_timer run schedule function uhc:time/min 60s