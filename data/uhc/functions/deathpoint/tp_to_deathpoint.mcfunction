# Execute as dead player after respawn
summon armor_stand ~ ~ ~ {Tags:["deathpoint_tp"],Marker:1b,PersistenceRequired:1b}
execute store result entity @e[type=armor_stand,tag=deathpoint_tp,limit=1] Pos[0] double 0.0142857 run scoreboard players get @s deathpoint.x
execute store result entity @e[type=armor_stand,tag=deathpoint_tp,limit=1] Pos[1] double 0.0001 run scoreboard players get @s deathpoint.y
execute store result entity @e[type=armor_stand,tag=deathpoint_tp,limit=1] Pos[2] double 0.0142857 run scoreboard players get @s deathpoint.z
execute at @e[type=armor_stand,tag=deathpoint_tp,limit=1] run tp @s ~ ~ ~
execute if score @s deathpoint_to_remove_forceload matches 1 at @s run forceload remove ~ ~
kill @e[type=armor_stand,tag=deathpoint_tp]
scoreboard players reset @s deathpoint_to_add_forceload
scoreboard players reset @s deathpoint_to_remove_forceload