execute as @a at @s run playsound entity.wither.spawn master @s ~ ~ ~
title @a title {"text":"Deathmatch!","color":"dark_red","bold":true}
execute store result score #num_players uhc_utils if entity @a[gamemode=!spectator]
title @a subtitle [{"score":{"name":"#num_players","objective":"uhc_utils"}},{"text":" players remaining","color":"gray"}]
spreadplayers 793.61 614.56 10 25 false @a[gamemode=!spectator]
tp @a[gamemode=spectator] 793.61 76 614.56