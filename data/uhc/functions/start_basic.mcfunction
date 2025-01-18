execute unless score #basic_start_confirmed uhc_config matches 1 run tellraw @s {"text":"Before starting in basic mode, make sure you have teleported all players to their spawn(s) and that the worldborder has been properly configured."}
execute unless score #basic_start_confirmed uhc_config matches 1 run tellraw @s [{"text":"Grace period, border shrink, and deathmatch will "},{"text":"not"},{"text":" be automatically triggered, so you must do so manually. Remaining time alerts will remain."}]
execute unless score #basic_start_confirmed uhc_config matches 1 run tellraw @s {"text":"If you are certain, run this command again to start the game in basic mode.","underlined":true,"clickEvent":{"action":"run_command","value":"/function uhc:start_basic"}}
execute unless score #basic_start_confirmed uhc_config matches 1 run scoreboard players set #basic_start_confirmed uhc_config 1

execute if score #basic_start_confirmed uhc_config matches 1 positioned 26520 178 -137 run function uhc:sequences/match_start_raw/match_start_1
execute if score #basic_start_confirmed uhc_config matches 1 run scoreboard players set #started_in_basic_mode uhc_config 1
execute if score #basic_start_confirmed uhc_config matches 1 run scoreboard players set #basic_start_confirmed uhc_config 0