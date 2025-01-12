effect give @a[gamemode=survival] blindness 4
execute positioned 26520 178 -137 run function uhc:spread_players

title @a title {"text":"3","bold":true,"color":"green"}
schedule function uhc:match_start_2 1s
schedule function uhc:match_start_3 2s
schedule function uhc:match_start_4 3s