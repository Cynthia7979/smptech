execute if score #match_started uhc_timer matches 1 as @a run function uhc:triggers/terminus_teleport
execute if score #match_started uhc_timer matches 1 as @a[gamemode=spectator] if score @s uhc_menu matches 1.. at @s run function uhc:terminus_menu
execute if score #match_started uhc_timer matches 1 as @a if score @s uhc_death matches 1.. run function uhc:on_death
# It's a one-off solution okay
execute if score #match_started uhc_timer matches 1 run function uhc:triggers/enable_all

execute store result score #border_size uhc_math run worldborder get
scoreboard players operation CurrentBorderSize: uhc_kills = #border_size uhc_math
