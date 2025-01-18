execute if score #match_started uhc_timer matches 1 as @a[gamemode=spectator] if score @s uhc_menu matches 1.. at @s run function uhc:triggers/terminus_menu
execute if score #match_started uhc_timer matches 1 unless score #tower_disabled uhc_config matches 1 as @a run function uhc:triggers/terminus_teleport
execute if score #match_started uhc_timer matches 1 if score #tower_disabled uhc_config matches 1 as @a[gamemode=spectator] run function uhc:triggers/terminus_teleport

execute if score #match_started uhc_timer matches 1 as @a unless score @s uhc_allow_tp_countdown matches -1 run function uhc:triggers/enable_towers
execute if score #match_started uhc_timer matches 1 as @a if score @s uhc_allow_tp_countdown matches -1 run function uhc:triggers/disable_towers
execute if score #match_started uhc_timer matches 1 as @a[gamemode=spectator] run scoreboard players enable @s uhc_menu