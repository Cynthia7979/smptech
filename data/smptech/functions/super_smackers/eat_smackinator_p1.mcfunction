playsound entity.generic.eat master @a ~ ~ ~
playsound entity.generic.eat master @a ~ ~ ~
playsound entity.generic.eat master @a ~ ~ ~
playsound entity.player.burp master @a ~ ~ ~
effect give @s minecraft:nausea 100 1 true
effect give @s minecraft:saturation 20
tellraw @s [{"text":"What have you done... You ","color":"yellow"},{"text":"ate ","italic":true},{"text":"the Smackinator?? It was ","italic":false},{"text":"cake ","italic":true},{"text":"all this time???","italic":false}]
tag @s add smptech.super_smackers.awaiting_eat_p2
schedule function smptech:super_smackers/eat_smackinator_p2 2s