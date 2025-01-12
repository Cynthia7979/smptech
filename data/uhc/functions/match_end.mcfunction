tag @a remove uhc_dead
gamemode spectator @a
schedule clear uhc:time/hour
schedule clear uhc:time/min
schedule clear uhc:time/sec
scoreboard players set #match_started uhc_timer 0
scoreboard players set @a uhc_allow_tp_countdown -2