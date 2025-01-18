function uhc:triggers/tick

execute if score #match_started uhc_timer matches 1 as @a if score @s uhc_death matches 1.. run function uhc:on_death

execute store result score #border_size uhc_math run worldborder get
scoreboard players operation CurrentBorderSize: uhc_kills = #border_size uhc_math

execute as @a[tag=uhc_dead,gamemode=!spectator] if score @s uhc_death_gamemode_cooldown matches 0 run gamemode spectator @s