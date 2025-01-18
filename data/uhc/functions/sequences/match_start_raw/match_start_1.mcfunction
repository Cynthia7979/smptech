clear @a[gamemode=!spectator]
gamemode survival @a[gamemode=!spectator]
xp set @a 0 levels
xp set @a 0 points
give @a[gamemode=!spectator] minecraft:filled_map{display: {Name: '{"text":"Map of Drehmal","italic":false}', MapColor: 3290191, Lore: ['{"text":"A map of the entire continent of","color":"dark_purple"}', '{"text":"Drehmal, showing the locations","color":"dark_purple"}', '{"text":"of its towns, major rivers,","color":"dark_purple"}', '{"text":"coastlines, and more.","color":"dark_purple"}', '{"text":" "}', '{"text":"Towns & Cities:","color":"gray","italic":false}', '{"text":"New Drabyel","color":"green"}', '{"text":"Okeke","color":"yellow"}', '{"text":"Ebonrun","color":"red"}', '{"text":"Athrah","color":"gold"}', '{"text":"Fort Nimahj","color":"dark_blue"}', '{"text":"Tharxax","color":"dark_red"}', '{"text":"Mohta","color":"aqua"}', '{"text":"Gozak","color":"dark_green"}', '{"text":"Firteid","color":"dark_aqua"}', '{"text":"Mossfield","color":"blue"}', '{"text":"Highfall","color":"dark_purple"}', '{"text":"Dusps","color":"light_purple"}']}, map: 103} 1

team join uhc_grace_period @a
scoreboard players set #match_started uhc_timer 1
function uhc:give_recipes
function uhc:time/begin
function uhc:add_players_to_scoreboards

time set day

title @a title [{"text":"Survive!","italic":true,"color":"white"}]
execute at @a as @s run playsound entity.elder_guardian.curse master @s ~ ~ ~