# Execute as dying player
# summon armor_stand ~ ~ ~ {Tags:["deathpoint_forceloader"],Marker:1b,PersistenceRequired:1b}
# execute store success score @s deathpoint_to_remove_forceload at @e[type=armor_stand,tag=deathpoint_forceloader,limit=1] run forceload query ~ ~
# scoreboard players operation @s deathpoint_to_add_forceload = @s deathpoint_to_remove_forceload
# execute if score @s deathpoint_to_add_forceload matches 1 at @e[type=armor_stand,tag=deathpoint_forceloader,limit=1] run forceload add ~ ~
# kill @e[type=armor_stand,tag=deathpoint_forceloader]

execute store result score @s deathpoint.x run data get entity @s LastDeathLocation.pos[0] 70
execute store result score @s deathpoint.y run data get entity @s LastDeathLocation.pos[1] 10000
execute store result score @s deathpoint.z run data get entity @s LastDeathLocation.pos[2] 70

summon armor_stand ~ ~ ~ {Tags:["deathpoint_forceloader"],Marker:1b,PersistenceRequired:1b}
execute store result entity @e[type=armor_stand,tag=deathpoint_forceloader,limit=1] Pos[0] double 0.0142857 run scoreboard players get @s deathpoint.x
execute store result entity @e[type=armor_stand,tag=deathpoint_forceloader,limit=1] Pos[1] double 0.0001 run scoreboard players get @s deathpoint.y
execute store result entity @e[type=armor_stand,tag=deathpoint_forceloader,limit=1] Pos[2] double 0.0142857 run scoreboard players get @s deathpoint.z
execute at @e[type=armor_stand,tag=deathpoint_forceloader,limit=1] run forceload add ~ ~
kill @e[type=armor_stand,tag=deathpoint_forceloader]