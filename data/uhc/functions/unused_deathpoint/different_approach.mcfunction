# Player should still be in survival right now
tp @s 5000 0 5000
setblock 5000 200 5000 minecraft:end_gateway{ExactTeleport:1b,ExitPortal:{X:0,Y:0,Z:0}}

execute store result score @s deathpoint.x run data get entity @s LastDeathLocation.pos[0] 1
execute store result score @s deathpoint.y run data get entity @s LastDeathLocation.pos[1] 1
execute store result score @s deathpoint.z run data get entity @s LastDeathLocation.pos[2] 1

execute store result block 5000 200 5000 ExitPortal.X int 1 run scoreboard players get @s deathpoint.x
execute store result block 5000 200 5000 ExitPortal.Y int 1 run scoreboard players get @s deathpoint.y
execute store result block 5000 200 5000 ExitPortal.Z int 1 run scoreboard players get @s deathpoint.z

tag @s remove deathpoint_just_died
tag @s add deathpoint_waiting_for_tp
schedule function uhc:deathpoint/teleport_dead_player 2t