# Run as player who died
execute at @a run playsound entity.ender_dragon.growl master @s ~ ~ ~

execute as @s at @s run function uhc:deathpoint/mark_deathpoint
tag @s add deathpoint_waiting_for_tp
schedule function uhc:deathpoint/initiate_deathpoint_tp 3s

tag @s add uhc_dead
gamemode spectator
scoreboard players set @s uhc_death 0
scoreboard players set @s uhc_allow_tp_countdown -2

title @s title {"text":"You died!","color":"dark_red"}
title @s subtitle {"text":"You may now spectate the game from Nothingness","color":"dark_gray"}
tellraw @s [{"text":"Type ","color":"dark_gray"},{"text":"/trigger uhc_menu","color":"aqua","hoverEvent":{"action":"show_text","value":[{"text":"Click to use command"}]},"clickEvent":{"action":"suggest_command","value":"/trigger uhc_menu"}},{"text":" to use Terminus teleportation!","color":"dark_gray"}]
tellraw @s [{"text":"Use your ","color":"dark_gray"},{"text":"hotbar","color":"white"},{"text":" to teleport to and spectate other players.","color":"dark_gray"}]