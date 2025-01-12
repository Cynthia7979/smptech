tellraw @a "[Av'UHC] Hello"

scoreboard objectives remove uhc_timer
scoreboard objectives add uhc_timer dummy
scoreboard objectives remove uhc_allow_tp_countdown
scoreboard objectives add uhc_allow_tp_countdown dummy

scoreboard objectives remove uhc_kills
scoreboard objectives add uhc_kills playerKillCount "Kills"
scoreboard players add @a uhc_kills 0
scoreboard objectives setdisplay sidebar uhc_kills

scoreboard objectives remove uhc_hp
scoreboard objectives add uhc_hp health "HP"
scoreboard players add @a uhc_hp 0
scoreboard objectives modify uhc_hp rendertype hearts
scoreboard objectives setdisplay belowName uhc_hp
scoreboard objectives setdisplay list uhc_hp

scoreboard objectives remove uhc_death
scoreboard objectives add uhc_death deathCount
scoreboard players set @a uhc_death 0

team remove uhc_grace_period
team add uhc_grace_period
team join uhc_grace_period @a
team modify uhc_grace_period friendlyFire false

worldborder damage amount 0

function uhc:triggers/add_triggers
function uhc:rng/init