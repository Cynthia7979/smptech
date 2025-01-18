scoreboard players add seconds uhc_timer 1

scoreboard players operation #sec_remaining uhc_timer = #seconds_end uhc_timer
scoreboard players operation #sec_remaining uhc_timer -= seconds uhc_timer

execute as @a if score @s uhc_allow_tp_countdown matches 0 run tellraw @s [{"text":"[ａｖＳＹＳ] Your Terminus session has expired.","color":"gray"}]
execute as @a if score @s uhc_allow_tp_countdown matches 0.. run scoreboard players remove @s uhc_allow_tp_countdown 1

# Deathpoint leftovers
# execute as @a unless score @s uhc_death_gamemode_cooldown matches 0 run scoreboard players remove @s uhc_death_gamemode_cooldown 1
# execute as @a if score @s uhc_death_gamemode_cooldown matches ..-1 run scoreboard players set @s uhc_death_gamemode_cooldown 0

execute unless score seconds uhc_timer >= #seconds_end uhc_timer run schedule function uhc:time/sec 1s