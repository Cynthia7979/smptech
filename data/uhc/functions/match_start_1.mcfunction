gamemode survival @a[gamemode=!spectator]
function uhc:rng/shuffle_towers
execute positioned 26520 178 -137 run function uhc:spread_players
clear @a[gamemode=!spectator]
give @a[gamemode=!spectator] minecraft:filled_map{display: {Name: '{"text":"Map of Drehmal","italic":false}', MapColor: 3290191, Lore: ['{"text":"A map of the entire continent of","color":"dark_purple"}', '{"text":"Drehmal, showing the locations","color":"dark_purple"}', '{"text":"of its towns, major rivers,","color":"dark_purple"}', '{"text":"coastlines, and more.","color":"dark_purple"}', '{"text":" "}', '{"text":"Towns & Cities:","color":"gray","italic":false}', '{"text":"New Drabyel","color":"green"}', '{"text":"Okeke","color":"yellow"}', '{"text":"Ebonrun","color":"red"}', '{"text":"Athrah","color":"gold"}', '{"text":"Fort Nimahj","color":"dark_blue"}', '{"text":"Tharxax","color":"dark_red"}', '{"text":"Mohta","color":"aqua"}', '{"text":"Gozak","color":"dark_green"}', '{"text":"Firteid","color":"dark_aqua"}', '{"text":"Mossfield","color":"blue"}', '{"text":"Highfall","color":"dark_purple"}', '{"text":"Dusps","color":"light_purple"}']}, map: 103} 1
team join uhc_grace_period @a
title @a title {"text":"3","bold":true,"color":"green"}
schedule function uhc:match_start_2 1s
schedule function uhc:match_start_3 2s
schedule function uhc:match_start_4 3s