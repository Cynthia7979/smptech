schedule clear uhc:time/hour
schedule clear uhc:time/min
schedule clear uhc:time/sec
schedule clear uhc:match_start_1
schedule clear uhc:match_start_2
schedule clear uhc:match_start_3
schedule clear uhc:match_start_4

function uhc:rng/init
scoreboard players set @a uhc_kills 0
scoreboard players set @a uhc_death 0
scoreboard players set #match_started uhc_timer 0

# Make it so Drehmal doesn't auto-teleport players from the world spawn to default map spawn
# Should only be necessary if someone triggered game start (will prob do it before event, manually)
scoreboard players set #game_started bool 0

worldborder damage amount 0
worldborder warning distance 0

gamemode survival @a
tp @a 26520 177 -92

tellraw @a "[Av'UHC] Match has been reset!"