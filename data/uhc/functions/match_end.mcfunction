execute as @a at @s run playsound entity.player.levelup master @s ~ ~ ~ 1 0.5
execute if entity @a[gamemode=survival] run title @a title [{"selector":"@p[gamemode=survival]","color":"yellow","bold":true},{"text":" is the winner!","bold":false,"color":"white"}]
execute unless entity @a[gamemode=survival] run title @a title [{"text":"nobody","color":"yellow","bold":true},{"text":" is the winner ","bold":false,"color":"white"},{"text":":(","color":"gray","bold":false}]
title @a subtitle {"text":"That's a wrap!"}
execute at @r[gamemode=survival] run summon firework_rocket ~ ~ ~ {Glowing:1b,LifeTime:15,FireworksItem:{id:"firework_rocket",Count:1,tag:{Fireworks:{Explosions:[{Type:2,Flicker:1b,Colors:[I;16771896,13208905]},{Type:4,Trail:1b,Colors:[I;3033289,2224383]},{Type:0,Colors:[I;1572778,1933397,5563391]},{Type:1,Colors:[I;7267071,10251263]}]}}}}
tag @a remove uhc_dead
gamemode spectator @a
schedule clear uhc:time/hour
schedule clear uhc:time/min
schedule clear uhc:time/sec
scoreboard players set #match_started uhc_timer 0
scoreboard players set @a uhc_allow_tp_countdown -2